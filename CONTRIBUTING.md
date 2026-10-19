# Contributing to oesu-playground

Thanks for being here! This repo exists so you can practise. Mistakes are wellcome.



1. Pick an issue, or find a problem yourself.
2. Comment **"Can I take this?"** on the issue so two people don't do the same wrok.
3. One issue = one small pull request.

## The workflow

```bash
# 1. Fork the repo on GitHub (button at the top right), then:
git clone https://github.com/<your-username>/oesu-playground.git
cd oesu-playground

# 2. Make a branch for your change
git checkout -b fix-readme-typo

# 3. Edit, then check the tests still pass
python -m pytest

# 4. Commit and push
git add .
git commit -m "Fix typo in README"
git push origin fix-readme-typo
```

5. Open a pull request on GitHub. Write `Fixes #<issue number>` in the description so the issue closes when it merges.

Tip: for a one-line docs fix you can skip all of this and press the ✏️ pencil icon on the file in GitHub.

## Reporting a bug

Use **New issue → Bug report**. A good report has:

- **Steps to reproduce**: the exact command you ran
- **Expected**: what should have happened
- **Actual**: what happened instead
- **Environment**: your OS and Python version

## Adding yourself to contributors

Create a new file `contributors/<your-github-username>.md` with one line about you. One file each means nobody gets merge conflicts.

## Stuck?

Ask in the ö-esu-esu WhatsApp group, or comment on your issue. Nobody minds questions.
