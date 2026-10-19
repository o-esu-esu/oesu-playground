"""textkit: tiny helpers for words and campus lief.

A practice project for ö-esu-esu sessions. Small on purpose, so you can
read all of it in ten minutes.
"""

from textkit.words import word_count, title_case, reverse_words
from textkit.checks import is_palindrome, is_anagram
from textkit.campus import classes_needed, cgpa_to_percentage

__all__ = [
    "word_count",
    "title_case",
    "reverse_words",
    "is_palindrome",
    "is_anagram",
    "classes_needed",
    "cgpa_to_percentage",
]

__version__ = "0.1.0"
