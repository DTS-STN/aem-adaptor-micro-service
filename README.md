# aem-adaptor-micro-service
An AEM adaptor to query, map and cache AEM responses

# Required Tooling

## Setup

### Install pipx:
```
python3 -m pip install --user pipx && python3 -m pipx ensurepath
```

### Install poetry:
```
pipx install poetry 
```

### Install application:
```
poetry install
```

### Setting up vscode:
install python extension, and add poetry's venv path to your vscode instance 
```
"python.venvFolders": [
  ".venv"
]
"python.venvPath": ".venv"
```

Restart vscode, then open the command palette and find "Python: Select Interpreter" and select the one with aem-adaptor-micro-service in the title.

## Package Management Actions

To test:
```
poetry run pytest
```

To run locally:
```
poetry run start
```

To add a library:
Non-development packages:
```
poetry add libraryname
```

Development packages:
```
poetry add --group dev libraryname

or

poetry add -G dev libraryname
```

## Required environment variables
AEM_GRAPHQL_ENDPOINT = "AEM's GraphQL endpoint"

APP_VERSION = "dts-aem-adaptor-ms/0.0.1"

## GraphQL query example
GraphQL queries are located at ./lib/graphql/queries/[project name]


Import query from GraphQL client and provide query path as a parametert (AEM example below).
```
from lib.graphql.client import query
aem_content = query("./lib/graphql/queries/sc-labs/home.graphql")
```