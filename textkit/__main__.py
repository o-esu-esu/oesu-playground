"""Command-line entry point: ``python -m textkit <command> ...``

Examples:
    python -m textkit count "open source is fun"
    python -m textkit palindrome level
    python -m textkit attendance 30 50
"""

import sys

from textkit import (
    word_count,
    title_case,
    reverse_words,
    is_palindrome,
    is_anagram,
    classes_needed,
    cgpa_to_percentage,
)

COMMANDS = {
    "count": lambda args: word_count(" ".join(args)),
    "title": lambda args: title_case(" ".join(args)),
    "reverse": lambda args: reverse_words(" ".join(args)),
    "palindrome": lambda args: is_palindrome(" ".join(args)),
    "anagram": lambda args: is_anagram(args[0], args[1]),
    "attendance": lambda args: classes_needed(int(args[0]), int(args[1])),
    "cgpa": lambda args: cgpa_to_percentage(float(args[0])),
}


def main(argv: list) -> int:
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print("usage: python -m textkit <command> [args]")
        print("commands: " + ", ".join(COMMANDS))
        return 1

    try:
        print(COMMANDS[argv[1]](argv[2:]))
    except ValueError:
        if argv[1] == "cgpa":
            print("error: CGPA must be a number")
        else:
            print("error: invalid argument")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
