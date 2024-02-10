# hive-cli

_A command line dictionary and word learning tool_

## Dev Steps

Refereneces: https://typer.tiangolo.com/tutorial/first-steps/

### Install the dependencies

```
pip install -r requirements.txt
```
Create venv: 
```
python3 -m venv .venv 
```

Start venv: 
```
source .venv/bin/activate
```



### How to update dependencies

Install pipreqs if you haven't

`pip install pipreqs`

Cd into the current project folder and use `--force` to overrwrite the current requirements.txt file.

`pipreqs ./ --force`

Reference: https://stackoverflow.com/questions/32390291/pip-freeze-for-only-project-requirements

Start application:
```
python main.py
```

## Architecture
