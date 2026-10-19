# Using textkit

Run every command from the project folder as `python -m textkit <command> [args]`.

| Command | Example | Output |
| --- | --- | --- |
| `count` | `python -m textkit count "open source is fun"` | `4` |
| `title` | `python -m textkit title "hello world"` | `Hello World` |
| `reverse` | `python -m textkit reverse "one two three"` | `three two one` |
| `palindrome` | `python -m textkit palindrome level` | `True` |
| `anagram` | `python -m textkit anagram listen silent` | `True` |
| `attendance` | `python -m textkit attendance 30 50` | `30` |
| `cgpa` | `python -m textkit cgpa 8` | `76.0` |

## attendance

Give it the classes you attended and the total classes so far, separated by a space. It tells you how many classes in a row you need to attend to reach 75%.

## cgpa

Converts a 10-point CGPA to a percentage using the common × 9.5 rule. If the CGPA is below 0 or above 10, an error has occurred and the tool stops.

## Using it from Python

```python
from textkit import word_count, classes_needed

word_count("open source is fun")   # 4
classes_needed(30, 50)             # 30
```
