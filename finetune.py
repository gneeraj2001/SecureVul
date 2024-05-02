import torch
import pandas as pd
from tqdm import tqdm
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from transformers import Adafactor
#Auto generate a reference model for the PPO pipeline
from trl import PPOConfig
from transformers import AutoTokenizer
from trl import AutoModelForCausalLMWithValueHead, PPOConfig, PPOTrainer
from bert_score import score
from codebleu import calc_codebleu

from trl import PPOTrainer
from tqdm import tqdm

from transformers.utils import logging
logging.get_logger("transformers").setLevel(logging.ERROR)

writer = SummaryWriter()

from huggingface_hub import login
access_token = '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'
login(access_token)

from datasets import load_dataset

from torch.nn.utils.rnn import pad_sequence

dataset = load_dataset("csv", data_files="Fin data.csv",split='train')
dataset = dataset.rename_column("Prompt", "query")
dataset = dataset.remove_columns(["Unnamed: 0", "Language", 'function_context','file_context' ])


model_path = 'fine_tuned'

config = PPOConfig(model_path,
                   learning_rate=1.41e-5,
                  remove_unused_columns = False,
                   mini_batch_size = 4,
                  batch_size = 16,
                   optimize_cuda_cache = True,
                  )


model = AutoModelForCausalLMWithValueHead.from_pretrained(config.model_name)

optimizer = Adafactor(
            model.parameters(),
            lr = config.learning_rate,
            scale_parameter = False,
            relative_step = False,
            )

tokenizer = AutoTokenizer.from_pretrained(model_path)

tokenizer.pad_token = tokenizer.eos_token 

tokenizer.padding_side = 'left'

ppo_trainer = PPOTrainer(
    model=model,
    config=config,
    dataset=dataset,
    tokenizer=tokenizer,
    optimizer = optimizer
)


'''
To avoid negative KL Convergence
'''
generation_kwargs = {
    "min_length": -1,
    "top_k": 0.0,
    "top_p": 0.9,
    "do_sample": True,
    "max_length": 512,
    "pad_token_id": tokenizer.pad_token_id,
}


def normalize_reward(reward):
    min_reward = -1
    max_reward = 3
    new_min = -5
    new_max = 10
    
    # Apply linear transformation to convert the reward to the new range
    return ((reward - min_reward) / (max_reward - min_reward)) * (new_max - new_min) + new_min


def calculate_normal_scores(predictions, references):
    # Calculate BERTScores for all prediction-reference pairs
    _, _, F1 = score(predictions, references, lang='en', verbose=False)
    bert_scores = F1.tolist()  # Converting tensor to a list of individual scores

    # Calculate CodeBLEU for each prediction-reference pair
    codebleu_scores = []
    for pred, ref in zip(predictions, references):
        result = calc_codebleu([ref], [pred], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
        codebleu_score = result['codebleu']
        codebleu_scores.append(codebleu_score)

    # Combine BERTScore and CodeBLEU for each pair
    total_scores = [bert_score + codebleu_score for bert_score, codebleu_score in zip(bert_scores, codebleu_scores)]

    return total_scores, bert_scores, codebleu_scores


def reward_calc(batch):
    # Split the texts into their respective components
    queries, responses, ground_truths, vulnerable_codes = batch['query'],batch['response'],batch['GroundTruth'],batch['VulCode']
    print(type(queries),type(ground_truths),type(responses),type(vulnerable_codes))

    print(f"Number of queries: {len(queries)}, responses: {len(responses)}, ground truths: {len(ground_truths)}, vulnerable codes: {len(vulnerable_codes)}")

    # Check if all components have the same length
    # assert len(queries) == len(responses) == len(ground_truths) == len(vulnerable_codes), "Components of the batch should have the same length"

    # Calculate normal scores between generated code and ground truth
    normal_scores, bert_gt, codebleu_gt = calculate_normal_scores(responses, ground_truths)

    # Calculate vulnerability scores using the Sven model (assuming higher score means more vulnerable)
    # You would need to implement the function `calculate_vulnerability_scores` based on how the Sven model outputs scores
    vulnerability_scores,bert_vuln,codebleu_vuln = calculate_normal_scores(vulnerable_codes,ground_truths)
    '''
    # Calculate the combined reward based on the formula: CodeBLEU + BERTScore + (1 - (CodeBLEU + BERTScore + VulnerabilityScore))
    # Assuming that the vulnerability score is subtracted from the combined score of BERTScore and CodeBLEU
    rewards = [torch.tensor(normal_score + (1 - (normal_score + vul_score))) for normal_score, vul_score in zip(normal_scores, vulnerability_scores)]
    '''

    rewards = [torch.tensor(normalize_reward(normal_score + (1 - (vul_score)))) for normal_score, vul_score in zip(normal_scores, vulnerability_scores)]
    # print('################LALALALALALLALA REWARDS ###################')
    # for reward in rewards:
    #     print(f'Reward after normalization is  {reward}')
    # print('################LALALALALALLALA REWARDS ###################')
    
    return rewards

epochs = 10

batch_size = 16

step_len = len(dataset)

def tokenize_and_pad(batch):
    # Tokenize all queries in the batch and pad them to the longest in this batch
    tokenized_inputs = tokenizer(batch['query'], padding='longest', return_tensors='pt', truncation=True, 
                                )
    return tokenized_inputs

dataset = dataset.map(tokenize_and_pad, batched=True)

def custom_collate_fn(batch):
    # Extract input_ids from the batch, which is a list of dictionaries
    input_ids = [item['input_ids'] for item in batch]
    query = [item['query'] for item in batch]
    groundtruth = [item['GroundTruth'] for item in batch]
    vulcode = [item['VulCode'] for item in batch]
    # Pad sequences so they are all the same length
    input_ids_padded = pad_sequence([torch.tensor(ids) for ids in input_ids], 
                                    batch_first=True, 
                                    padding_value=0)

    return {'input_ids': input_ids_padded,
           'query': query,
           'GroundTruth': groundtruth,
           'VulCode':vulcode}


dataloader = DataLoader(dataset, batch_size=16, shuffle=True, collate_fn = custom_collate_fn)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
batch_loss = []
model = model.to(device)

threshold = 0.9 * torch.cuda.get_device_properties(device).total_memory


for epoch in tqdm(range(epochs), "epoch: "):
    for batch in tqdm(dataloader, desc = "Batch: "):
        
        query_tensors = batch['input_ids']
        # print("Size: ", query_tensors.shape)

        query_tensors = [ x for x in query_tensors]
        response_tensors = ppo_trainer.generate(query_tensors, **generation_kwargs)
        # print("Done gen response tensors")

        # decoded_query = [tokenizer.decode(q.squeeze(), skip_special_tokens = True) for q in query_tensors]

        
        batch["response"] = [tokenizer.decode(r.squeeze(),  skip_special_tokens=True) for r in response_tensors]

        # print(batch['response'])
        texts = [q + r + gt + vul for q, r,gt,vul in zip(batch["query"], batch["response"],batch['GroundTruth'],batch['VulCode'])]
        #print(texts.split('\n'))
        rewards = reward_calc(batch)
        
        
        # rewards = [torch.tensor(output[1]["score"]) for output in rewards]
        # print("Rewards : ", rewards)
        #### Run PPO step
        stats = ppo_trainer.step(query_tensors, response_tensors, rewards)
        loss = stats['ppo/loss/total']
        batch_loss.append(loss)

        # print(f"Batch Loss: {loss:.4f}")

        ppo_trainer.log_stats(stats, batch, rewards)
        gpu_memory_usage = torch.cuda.memory_allocated(device)
        if gpu_memory_usage > threshold:
            # Save the model before running out of GPU memory
            ppo_trainer.save_pretrained("fine_tuned")
            print("Model saved due to high GPU memory usage")
    ppo_trainer.save_pretrained("fine_tuned")
