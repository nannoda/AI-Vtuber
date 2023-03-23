import asyncio
from transformers import GPTNeoXForCausalLM, AutoTokenizer


async def main():
    model = GPTNeoXForCausalLM.from_pretrained(
        "EleutherAI/pythia-70m-deduped",
        revision="step3000",
        cache_dir="./pythia-70m-deduped/step3000",
    )

    tokenizer = AutoTokenizer.from_pretrained(
        "EleutherAI/pythia-70m-deduped",
        revision="step3000",
        cache_dir="./pythia-70m-deduped/step3000",
    )

    inputs = tokenizer(
        "The following is a conversation between a vtuber and her chat.\nChat: Hello, vtuber!\n Vtuber: Hello, chat!",
        return_tensors="pt",
        max_length=1024,
        truncation=True,
    )
    tokens = model.generate(**inputs, max_length=128, do_sample=True, top_p=0.95, top_k=60, temperature=0.9)
    tokenizer.decode(tokens[0])
    print(tokenizer.decode(tokens[0]))


if __name__ == "__main__":
    asyncio.run(main())
