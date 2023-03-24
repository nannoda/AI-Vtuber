from transformers import GPTNeoXForCausalLM, AutoTokenizer

model = GPTNeoXForCausalLM.from_pretrained(
    "EleutherAI/pythia-1b-deduped",
    revision="step3000",
    cache_dir="./pythia-1b-deduped/step3000",
)

tokenizer = AutoTokenizer.from_pretrained(
    "EleutherAI/pythia-1b-deduped",
    revision="step3000",
    cache_dir="./pythia-1b-deduped/step3000",
)

inputs = tokenizer("Hello, I am Nezumiya Chinoha, a vtuber", return_tensors="pt")
tokens = model.generate(**inputs, do_sample=True, min_length=20, max_length=128, top_k=50, top_p=0.95, temperature=0.9)
out = tokenizer.decode(tokens[0])

print(tokens)
print(out)
