from textkit.checks import is_palindrome, is_anagram


def test_palindrome_true():
    assert is_palindrome("level")


def test_palindrome_false():
    assert not is_palindrome("python")


def test_palindrome_with_spaces():
    assert is_palindrome("nurses run")


def test_anagram_true():
    assert is_anagram("listen", "silent")


def test_anagram_false():
    assert not is_anagram("python", "java")


def test_anagram_case_and_spaces():
    assert is_anagram("Dormitory", "dirty room")


def test_anagram_empty():
    assert is_anagram("", "")



def test_palindrome_with_capital_letters():
    assert is_palindrome("Race car")
    assert is_palindrome("Madam")
