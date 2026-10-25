import subprocess, sys
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="local")

diff = subprocess.run(["git", "diff"], capture_output=True, text=True).stdout
if not diff.strip():
    sys.exit("No uncommitted changes to review.")

resp = client.chat.completions.create(
    model="qwen2.5-coder:7b",
    messages=[
        {"role": "system", "content": "You are a code reviewer. Point out bugs, unclear names and missing tests. Be short, use bullet points."},
        {"role": "user", "content": diff[:12000]},
    ],
)
print(resp.choices[0].message.content)