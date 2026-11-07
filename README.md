\# DV066G – Running local LLMs with Ollama



Group 17: Muntaser Ibrahim



\## Models used

\- llama3.2:1b (Meta, \~1.3 GB)

\- qwen2.5:0.5b (Alibaba, \~400 MB)



\## How to run

1\. Install Ollama: https://ollama.com/download

2\. Pull the models:

&#x20;  ollama ```pull llama3.2:1b```

&#x20;  ollama ```pull qwen2.5:0.5b```

3\. Install the Python library:

&#x20;  pip install ollama

4\. Run the script:

&#x20;  python main.py



The script sends the same prompt to both models and saves the model name,

prompt, response and response time to `outputs.csv`.



\## Observations

\*\*Speed:\*\* 

On the first run, qwen2.5:0.5b took 1.42 seconds and llama3.2:1b took 3.84 seconds. This makes sense because qwen is much smaller (\~400 MB) than llama (\~1.3 GB). Because qwen has less than half the parameters, my PC  processes it much faster.


\*\*Correctness:\*\* Both answers were correct but qwen2.5:0.5b was accurate on basic facts, but its answer was very short, it only mentioned using a hash function for efficient retrieval of elements by key.



\*\*Repeated runs:\*\* Running the script 2–3 more times produced slightly different wording and sentence structures each time, even though the core facts stayed the same.


\*\*Compared to commercial models:\*\* 
Compared to Claude ,Large cloud models, give far richer explanations.
Small local models are good when it comes to safety of data since code and data never leave my PC.

