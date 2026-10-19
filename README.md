# oesu-playground 🐧

A tiny Python projetc for **ö-esu-esu** sessions. Use it to practise finding your way around a codebase and making your first open-source contributon.

`textkit` has a few small helpers: counting words, checking palindromes, and working out how many classes you need to reach 75% attendance. conflicts

> 💡 This repo has a few **deliberate mistakes**: typos, missing steps, hidden bugs and missing tests. Finding and fixing them is the point!

## What you need

- Python 3.9 or newer
- Git
- A GitHub account

## Try it

Clone the repo and run the tool from the project folder:

```bash
git clone https://github.com/o-esu-esu/oesu-playground.git
cd oesu-playground
python -m textkit count "open source is fun"
python -m textkit attendance 30 50
```

You should recieve an awer straight away. See [docs/usage.md](docs/usage.md) for every command.

## Run the tests

First install the test :

```bash
pip install -r requirements-dev.txt
```

Then run the suite:

```bash
python -m pytest
```

Every pull request runs the tests automatically, so you will see a ✅ or ❌ on your PR.

## Project layout

| Path | What's inside |
| --- | --- |
| `textkit/` | the code |
| `tests/` | the tests (pytest) |
| `docs/` | longer documentation |
| `contributors/` | one file per contributor, add yours! |
| `.github/` | issue templates, PR template and the test workflow |

## Contributing

New here? Start with [CONTRIBUTING.md](CONTRIBUTING.md), then try the [treasure hunt](TREASURE_HUNT.md).
Look for issues labelled **good first issue**.

## Code of Conduct

Be kind. Read our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE)
