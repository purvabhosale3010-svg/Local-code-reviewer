# Local Code Reviewer

A small Python tool that reviews your uncommitted git changes using an
open-weight AI model running on your own computer. No cloud, no API key,
no cost. Your code never leaves your machine.

Built for Hacktoberfest 2026 (Open source AI).

## Why open matters
- **Privacy:** your code stays on your laptop
- **Offline:** works without internet
- **Cost:** no per-token bill
- **Control:** you can swap in any model Ollama supports

## How it works
1. `review.py` runs `git diff` to collect your uncommitted changes
2. It sends them to a local model through Ollama's OpenAI-compatible API
3. It prints a short review: bugs, unclear names and missing tests

The three layers:
- **Weights:** `qwen2.5-coder:7b` (open-weight coding model)
- **Runtime:** Ollama
- **Harness:** `review.py`

## Requirements
- [Ollama](https://ollama.com/download)
- [Git](https://git-scm.com/downloads)
- Python 3
- About 5 GB of free disk space for the model
- 8 GB RAM recommended (for 4 GB RAM, use `gemma3:4b` instead)

## Setup
```
ollama pull qwen2.5-coder:7b
python -m pip install openai
```

## Usage
Make sure the Ollama app is running, then inside any git repo with
uncommitted changes:
```
python review.py
```

## Example
`test.py` contains a deliberately buggy `add` function (it subtracts)
and a `divide` function with no zero check:
```
- The function name `add` is misleading; it should probably be `subtract`.
- Missing tests for the `divide` function.
- The function `divide` should handle the case when `b` is zero.
```

## Limitations
- A small 7B model is less accurate than large hosted models. In the
  example above it caught the missing zero check and missing tests,
  but suggested renaming `add` instead of fixing the bug.
- It only reviews changes to files git already tracks. Brand-new
  untracked files are not included.
- Very large diffs are cut off at 12,000 characters.

## What's next
- Review new (untracked) files
- Save reviews to a file
- Choose the model with a command-line option
- An offline assistant that explains medical reports and government
  forms in Hindi and Marathi

## Author
PP