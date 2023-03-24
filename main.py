import asyncio
from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

prompt = """
This is how a toxic entitled evil female streamer responded in a conversation. She would respond in a toxic and rude manner. She would talk about the message and would elaborate on it as well as share some of her experiences if possible. She would also go on a tangent if possible.
"""


def generate_response(chat_text: str) -> str:
    input_text = prompt + "Chat: " + chat_text + "\nstreamer:"
    out = generator(input_text,
                    do_sample=True,
                    min_length=20,
                    max_length=128,
                    top_k=50,
                    top_p=0.95,
                    temperature=0.9,
                    )[0]['generated_text']
    return out.split("streamer:")[1]


async def main():
    while True:
        chat_text = input("You: ")

        if chat_text == "exit":
            break

        response = generate_response(chat_text)
        print(f"Bot: {response}")


if __name__ == "__main__":
    asyncio.run(main())
