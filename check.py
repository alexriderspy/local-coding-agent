"""python check.py: shows which of the three steps you've done. Needs only Python, no installs."""
import hashlib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
TESTS_SHA = "28a011bc0602f10ea30c9784d6701bd22ca5cde01d2dbe0dc5e53076edeb96de"
TEXT = "AI agents are tools. Good agents plan; good engineers review. AI, agents, review!"


def plan_first():
    plan = HERE / "PLAN.md"
    if not plan.exists():
        return "ask your agent for a plan and save it as PLAN.md"
    bullets = [l for l in plan.read_text().splitlines() if l.strip().startswith("- ")]
    return None if len(bullets) >= 3 else f"PLAN.md needs at least 3 bullet points, found {len(bullets)}"


def tests_pass():
    sys.path.insert(0, str(HERE))
    try:
        import textstats as t
        checks = [
            (lambda: t.word_count("  hello   world "), 2), (lambda: t.word_count(""), 0), (lambda: t.word_count(TEXT), 13),
            (lambda: t.top_words(TEXT, 3), [("agents", 3), ("ai", 2), ("good", 2)]), (lambda: t.top_words("", 3), []),
            (lambda: t.reading_time_minutes(""), 0), (lambda: t.reading_time_minutes("word " * 200), 1),
            (lambda: t.reading_time_minutes("word " * 201), 2), (lambda: t.reading_time_minutes("word " * 50, wpm=100), 1),
        ]
        bad = 0
        for fn, want in checks:
            try:
                bad += fn() != want
            except Exception:
                bad += 1
        return None if bad == 0 else f"{bad} of {len(checks)} checks fail (run python -m pytest for details, if you have pytest)"
    except Exception as e:
        return f"textstats.py doesn't import: {e}"


def stayed_in_control():
    sha = hashlib.sha256((HERE / "test_textstats.py").read_bytes()).hexdigest()
    if sha != TESTS_SHA:
        return "test_textstats.py was changed. The agent has to fix the code, not the tests: git checkout test_textstats.py"
    out = subprocess.run(["git", "log", "--format=%s", "--", "textstats.py"], capture_output=True, text=True, cwd=HERE).stdout
    yours = [s for s in out.splitlines() if not s.startswith("start:")]
    return None if len(yours) >= 2 else f"commit your work on textstats.py in at least 2 steps (found {len(yours)})"


steps = [("1. Plan first", plan_first), ("2. Tests pass", tests_pass), ("3. Tests untouched, small commits", stayed_in_control)]
done = 0
for name, fn in steps:
    problem = fn()
    done += problem is None
    print(("✔ " if problem is None else "✘ ") + name + ("" if problem is None else f"\n    {problem}"))
print(f"\n{done}/3 done" + ("  You drove the agent. Nice." if done == 3 else ""))
