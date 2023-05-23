# {{cookiecutter.module_display_name}}

**MODULE OVERVIEW**:

<a href="https://github.com/defi-engine/{{cookiecutter.module_display_name}}/blob/master/LICENSE">
  <img alt="GitHub" src="https://img.shields.io/github/license/defi-engine/{{cookiecutter.module_display_name}}">
</a>

<a href="https://github.com/charliermarsh/ruff">
  <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json">
</a>

## {{cookiecutter.module_description}}

### how to start
install dependencies and activate environment
```
poetry install
poetry shell
```
run postgres database
```
docke-compose up -d
```
run fastAPI app
```
poetry run app
```
