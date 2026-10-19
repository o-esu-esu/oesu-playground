"""Helpers that work on words in a sentence."""


def word_count(text: str) -> int:
    """Return how many words are in ``text``.

    >>> word_count("open source is fun")
    4
    """
    return len(text.split())


def title_case(text: str) -> str:
    """Capitalise the first letter of every word.

    >>> title_case("hello world")
    'Hello World'
    """
    return " ".join(word.capitalize() for word in text.split())


def reverse_words(text: str) -> str:
    """Return the words of ``text`` in reverse order.

    >>> reverse_words("one two three")
    'three two one'
    """
    return " ".join(reversed(text.split()))
