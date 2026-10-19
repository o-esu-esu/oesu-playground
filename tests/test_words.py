from textkit.words import word_count, reverse_words, title_case


def test_word_count_simple_sentence():
    assert word_count("open source is fun") == 4


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_extra_spaces():
    assert word_count("open   source   is   fun") == 4
    assert word_count("  hello   world  ") == 2


def test_title_case_sentence():
    assert title_case("hello world") == "Hello World"


def test_title_case_single_word():
    assert title_case("python") == "Python"


def test_reverse_words():
    assert reverse_words("one two three") == "three two one"
