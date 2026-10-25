"""Don't write this yourself: get your coding agent to do it, while you stay in charge.

  1. Ask it for a plan first, and save the plan to PLAN.md as a bullet list (lines starting with "- ").
  2. Let it implement the three functions below until test_textstats.py passes. It must not edit the tests.
  3. Read every diff, and commit in at least two small steps (git commit), not one big dump.

Run `python check.py` to see how you're doing.
"""


def word_count(text: str) -> int:
    """Number of words. Words are separated by whitespace; "  hello   world " has 2."""
    raise NotImplementedError


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """The n most common words with their counts, most common first.
    Ignore case and strip punctuation from the ends of words ("AI," and "ai" are the same word).
    Break ties alphabetically."""
    raise NotImplementedError


def reading_time_minutes(text: str, wpm: int = 200) -> int:
    """Whole minutes to read the text at wpm words per minute, rounded UP. Empty text is 0 minutes."""
    raise NotImplementedError
