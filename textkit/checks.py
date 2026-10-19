"""Yes/no checks on words."""


def is_palindrome(word: str) -> bool:
    """Return True if ``word`` reads the same forwards and backwards.

    Spaces and capital letters are ignored, so "Race car" counts.

    >>> is_palindrome("level")
    True
    """
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def is_anagram(first: str, second: str) -> bool:
    """Return True if ``first`` and ``second`` use exactly the same letters.

    Spaces and capital letters are ignored.

    >>> is_anagram("listen", "silent")
    True
    """
    def letters(s: str) -> list:
        return sorted(s.replace(" ", "").lower())

    return letters(first) == letters(second)
