## black
```aiignore
✗ black exercise.py 
reformatted exercise.py

All done! ✨ 🍰 ✨
1 file reformatted.
```
Is is the formatter to format the .py files standardly.


## build

## build-backend

## ruff

## mypy

## bandit



## something for later
```aiignore
# .github/workflows/ci.yml
name: Lint and Type Check

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          pip install pdm
          pdm install --dev

      - name: Run Black
        run: |
          pdm run black --check .

      - name: Run Ruff
        run: |
          pdm run ruff check .

      - name: Run mypy
        run: |
          pdm run mypy .

      - name: Run Bandit
        run: |
          pdm run bandit -c pyproject.toml -r .

```