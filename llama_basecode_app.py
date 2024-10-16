## https://penguincloud.tistory.com/entry/Meta%EC%9D%98-Llama-32-%EB%8B%A4%EA%B5%AD%EC%96%B4-AI-%EB%AA%A8%EB%8D%B8%EC%9D%98-%EC%83%88%EB%A1%9C%EC%9A%B4-%EC%8B%9C%EB%8C%80
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://<Your IP>:5555/v1", api_key="lm-studio")


completion = client.chat.completions.create(
  model="lmstudio-community/Llama-3.2-3B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
