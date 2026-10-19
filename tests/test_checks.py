from textkit.checks import is_palindrome, is_anagram


def test_palindrome_true():
    assert is_palindrome("level")


def test_palindrome_false():
    assert not is_palindrome("python")


def test_palindrome_with_spaces():
    assert is_palindrome("nurses run")


def test_palindrome_with_capital_letters():
    assert is_palindrome("Race car")
    assert is_palindrome("Madam")


def test_is_anagram_true():
    assert is_anagram("listen", "silent")


def test_is_anagram_false():
    assert not is_anagram("hello", "world")


def test_is_anagram_with_spaces_and_caps():
    assert is_anagram("Dormitory", "dirty room")
