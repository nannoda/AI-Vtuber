"""
This is a server that host a language model.
It is a simple wrapper around the transformers library.

The server is a simple flask app that exposes a single endpoint /generate.
"""

import argparse
import json
import os
import flask

from transformers import pipeline

name = "Language Model Server"

app = flask.Flask(name)

generator = None


def generate_text(text,
                  temperature: float = 0.9,
                  top_k: int = 50,
                  top_p: float = 0.95,
                  do_sample: bool = True,
                  max_length: int = 128,
                  min_length: int = 20,
                  ):
    global generator
    if generator is None:
        raise ValueError("Generator is not initialized")
    try:
        out = generator(text,
                        do_sample=do_sample,
                        min_length=min_length,
                        max_length=max_length,
                        top_k=top_k,
                        top_p=top_p,
                        temperature=temperature,
                        )
        out = out[0]["generated_text"]
        return out
    except Exception as e:
        return {"error": str(e)}


@app.route("/api/post/gen", methods=["POST"])
def generate():
    data = flask.request.get_json()
    text = data["text"]
    temperature = data.get("temperature", 0.9)
    top_k = data.get("top_k", 50)
    top_p = data.get("top_p", 0.95)
    do_sample = data.get("do_sample", True)
    max_length = data.get("max_length", 128)
    min_length = data.get("min_length", 20)

    out = generate_text(text, temperature=temperature, top_k=top_k, top_p=top_p, do_sample=do_sample, max_length=max_length,
                        min_length=min_length)
    return flask.jsonify(out)

@app.route("/api/get/gen", methods=["GET"])
def generate_get():
    data = flask.request.args
    text = data["text"]
    temperature = data.get("temperature", 0.9)
    top_k = data.get("top_k", 50)
    top_p = data.get("top_p", 0.95)
    do_sample = data.get("do_sample", True)
    max_length = data.get("max_length", 128)
    min_length = data.get("min_length", 20)

    out = generate_text(text, temperature=temperature, top_k=top_k, top_p=top_p, do_sample=do_sample, max_length=max_length,
                        min_length=min_length)
    return flask.jsonify(out)


def main():
    global generator
    parser = argparse.ArgumentParser()
    parser.add_argument( "--model", type=str, default="EleutherAI/gpt-neo-1.3B",
                        help="The model to use, e.g. EleutherAI/gpt-neo-1.3B. "
                             "See https://huggingface.co/models for more models.")
    parser.add_argument("--port", type=int, default=6060, help="The port to use")
    args = parser.parse_args()
    generator = pipeline("text-generation", model=args.model)
    app.run(port=args.port)


if __name__ == "__main__":
    main()
