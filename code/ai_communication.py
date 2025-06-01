#nettisivu troubleshoottaamista ja parannuksia varten https://docs.datacrunch.io/containers/tutorials/deploy-with-vllm-indepth#test-deployment

import os
import requests
import sys
import signal
from api_key import KEY as key
from address import ADDRESS as address
from instructions import INSTRUCTIONS as instructions
import pdf_to_text

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def request(user_input,type) -> None:
    url = address+'v1/completions'
    text=pdf_to_text.extract_text_from_pdf(get_filepath())
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+key,
    }
    if type == "general":
        data = {
            "model": "deepseek-ai/deepseek-llm-7b-chat",
            "prompt": f"{user_input}",
            "max_tokens": 128,
            "temperature": 0.7,
            "top_p": 0.9
        }

    else:
        data = {
            "model": "deepseek-ai/deepseek-llm-7b-chat",
            "prompt": f"Here is an information sheet to use:{text} Here are the instructions to handling user input: {instructions} Here is the user input: {user_input}",
            "max_tokens": 128,
            "temperature": 0.7,
            "top_p": 0.9
        }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Response content is not valid JSON.", file=sys.stderr)
            print("Response body:", file=sys.stderr)
            print(response.text, file=sys.stderr)
            return None
    else:
        print(f"Request failed with status code {response.status_code}", file=sys.stderr)
        print("Response body:", file=sys.stderr)
        print(response.text, file=sys.stderr)
        return None
    
def get_filepath():
    absolute_path = os.path.dirname(__file__)
    relative_path = r"../Case/Wartsila_engine.pdf"
    filepath = os.path.join(absolute_path, relative_path)
    return filepath

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)