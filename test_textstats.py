"""The agent must make these pass WITHOUT editing this file."""
from textstats import reading_time_minutes, top_words, word_count

TEXT = "AI agents are tools. Good agents plan; good engineers review. AI, agents, review!"


def test_12_2_word_count():
    assert word_count("  hello   world ") == 2
    assert word_count("") == 0
    assert word_count(TEXT) == 13


def test_12_2_top_words():
    assert top_words(TEXT, 3) == [("agents", 3), ("ai", 2), ("good", 2)]
    assert top_words("", 3) == []


def test_12_2_reading_time():
    assert reading_time_minutes("") == 0
    assert reading_time_minutes("word " * 200) == 1
    assert reading_time_minutes("word " * 201) == 2
    assert reading_time_minutes("word " * 50, wpm=100) == 1
