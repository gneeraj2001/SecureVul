Fine-tuning an LLM to produce more robust and non-vulnerable code using Reinforcement Learning. 
We fine-tune Starcoderbase 1b using a custom reward function and compare its performance v/s the base starcoder before fine-tuning.
We use SVEN to generate vulnerable code given a prompt using the aise_gen.py script. The dataset is a filtered and modified version of the [CyberNative/Code_Vulnerability_Security_DPO](https://huggingface.co/datasets/CyberNative/Code_Vulnerability_Security_DPO) dataset where we filter the C/C++ and Python prompts and convert it into the file context and function context prompt format as expected by SVEN.

To run the fine-tuning script run finetune.py script, and to run inference on starcoder run the starcoderinference.py script. 

To check for vulnerabilities in generated code using CodeQL, the following steps need to be followed:

1) Download codeql  `wget https://github.com/github/codeql-action/releases/download/codeql-bundle-v2.17.0/codeql-bundle-linux64.tar.gz`
2) Untar downloaded file
3) Add CodeQL executable to the PATH variable
4) Create a src folder with all scripts that need to be checked
5) Run scripts to remove scripts that don't compile.
6) Execute ./run.sh
