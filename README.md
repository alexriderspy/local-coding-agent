# Free coding agent on your laptop

Claude Code, running on a small local model with [Ollama](https://ollama.com). No API key, no card.

## Setup (10 minutes)

1. **Install Ollama** from [ollama.com/download](https://ollama.com/download) and open it.
2. **Get the model** (2.7 GB):
   ```bash
   ollama pull qwen3.5:2b
   ```
3. **Give it more memory:** Ollama app → Settings → Context length → **32k**. (At the default 4k the agent forgets what it's doing.)
4. **Install Claude Code:**
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   Windows: `irm https://claude.ai/install.ps1 | iex`

## The exercise

```bash
git clone https://github.com/alexriderspy/local-coding-agent.git
cd local-coding-agent
ollama launch claude --model qwen3.5:2b
```

Then give it one small job at a time:

1. *"Read textstats.py. Don't write code. Write a plan as bullet points in PLAN.md."*
2. *"Implement word_count only. Don't edit test_textstats.py."* Read the diff, then `git commit -am "word_count"`.
3. *"Now top_words."* Read, commit. Then *"Now reading_time_minutes."* Read, commit.

Check yourself any time with `python check.py`. You're done at 3/3.

## Good to know

- A small model makes mistakes. Read every diff. If a check fails, paste the error back to it.
- If it edits the tests, undo with `git checkout test_textstats.py` and tell it to fix the code.
- Slow? Close Chrome. It needs about 7 GB of free memory.
