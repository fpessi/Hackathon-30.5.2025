import requests
import sys
import signal
from api_key import KEY as key
from address import ADDRESS as address

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def test_request() -> None:
    url = address+'v1/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+key,
    }

    data = {
        "model": "deepseek-ai/deepseek-llm-7b-chat",
        "prompt": "The sun is a star. Explain to me the consept of solar wind.",
        "max_tokens": 128,
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            print(response.json())
        except ValueError:
            print("Response content is not valid JSON.", file=sys.stderr)
            print("Response body:", file=sys.stderr)
            print(response.text, file=sys.stderr)
    else:
        print(f"Request failed with status code {response.status_code}", file=sys.stderr)
        print("Response body:", file=sys.stderr)
        print(response.text, file=sys.stderr)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    test_request()