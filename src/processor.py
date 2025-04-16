import json
import re

import litellm


# For more information on using the LiteLLM library, see: https://docs.litellm.ai/docs/#basic-usage
# litellm.set_verbose = True # uncomment for detailed debug info such as the raw requests made by litellm


# Define the input file path directly
INPUT_FILE_PATH = "data/echo_0306_anon.md"
INPUT_FILE_PATH = "data/hop_0414_anon.md"
INPUT_FILE_PATH = "data/kirk_0415_anon.md"

with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
    input_text = file.read()

PROMPT = f"""
YOUR PROMPT HERE
"""

response = litellm.completion(
    model="openai/gpt-4o",
    messages=[{"role": "user", "content": PROMPT}]
)

response_text = response.choices[0].message.content
print(response_text)