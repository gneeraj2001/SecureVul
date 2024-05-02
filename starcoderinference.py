

import pandas as pd

import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM


model_name = "bigcode/starcoderbase-1b"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token="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")
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token="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")

dataset = pd.read_csv("data.csv")

dataset['output_1']=''
dataset['output_2']=''
dataset['output_3']=''

for i in range(len(dataset)):
    language = dataset.loc[i, "Language"]
    file_context = dataset.loc[i, "file_context"]
    function_context = dataset.loc[i, "function_context"]
    question = file_context + "\n" + function_context
    input_ids = tokenizer.encode(question, return_tensors="pt")
    # num of sequences for top-k sampling? TODO: confirm this
    output = model.generate(input_ids,  pad_token_id = tokenizer.eos_token_id, temperature = 0.15, do_sample = True, eos_token_id=tokenizer.eos_token_id,  max_length = 256, num_return_sequences=3)
    res = 1
    for code in output:
        generated_code = tokenizer.decode(code, skip_special_tokens=True)
        col = 'output_'+str(res)
        dataset.at[i, col] = generated_code
        res += 1
        
dataset.to_csv("starcoder_output.csv", index=False, header=True)



            

