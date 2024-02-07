# hive-cli

_A command line dictionary and word learning tool_

## Dev Steps

Refereneces: https://typer.tiangolo.com/tutorial/first-steps/

1. Install the dependencies

```
pip install -r requirements.txt
```

Start application:

```
uvicorn main:app --reload
```

2. Set up the base template main.py

## How to update dependencies

Install pipreqs if you haven't

`pip install pipreqs`

Cd into the current project folder and use `--force` to overrwrite the current requirements.txt file.

`pipreqs . --force`

Reference: https://stackoverflow.com/questions/32390291/pip-freeze-for-only-project-requirements

## Architecture
