import csv, time, ollama

PROMPT = "Explain what a hash table is in two sentences."
MODELS = ["llama3.2:1b", "qwen2.5:0.5b"]

rows = []
for model in MODELS:
    start = time.time()
    r = ollama.chat(model=model, messages=[{"role": "user", "content": PROMPT}])
    rows.append({"model": model, "prompt": PROMPT,
                 "response": r["message"]["content"],
                 "seconds": round(time.time() - start, 2)})

with open("outputs.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)