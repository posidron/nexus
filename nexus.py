#!/usr/bin/env python3
# pylint: disable=C0103
import os
import sys
from typing import Union

import openai

MAX_TOKENS = 1024
MODEL_MAX_LIMIT = 4097

def nexus(arg: str, pipe: str) -> Union[str,None]:
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        print("OPENAI_API_KEY is not set")
        sys.exit(1)
    user_prompt = f"{arg}\n{pipe}"
    try:
        result = openai.Completion.create(
            engine="text-davinci-003", prompt=user_prompt, max_tokens=MAX_TOKENS
        )
    except openai.error.ServiceUnavailableError as error:
        print(error)
        sys.exit(1)
    return result["choices"][0]["text"].strip()

if __name__ == "__main__":
    pipe = ""
    if not os.isatty(0):
        pipe = sys.stdin.read()
        pipe = pipe[:MODEL_MAX_LIMIT]
    argument = ""
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        argument = argument[:MODEL_MAX_LIMIT]
    if not pipe and not argument:
        print("Usage: nexus [argument] < [pipe]")
        sys.exit(1)
    print(nexus(argument, pipe))
