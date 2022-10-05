# aem-adaptor-micro-service
An AEM adaptor to query, map and cache AEM responses

# Required Tooling

## Python Version:
The package manager we are using, poetry, requires python 3.7+

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

## Starting the cache locally

### Install docker-compose.

You can either install docker-compose via your Operating System's package manager, or via pip.

```
pip install docker-compose
```

### Building and Starting the local cache container

```
docker-compose up -d redis
```

If you are running the application locally, ensure that the REDIS_HOST env var, in your .env file is set to 127.0.0.1.

If you are running the application in a container, ensure that the REDIS_HOST env var, in your .env file is set to redis.


## Required environment variables
AEM_GRAPHQL_ENDPOINT = "AEM's GraphQL endpoint"

APP_VERSION = "dts-aem-adaptor-ms/0.0.1"

## Creating a new query

### Adding an endpoint
Create a new route in your projects /app/router file

Example
```
@router.get("/home")
async def read_sch_get_home():
    return sch_content.get_home()
```

### Adding a content function
Create a content function in your projects /app/content file

Example
```
def get_home():
    aem_content = query("./lib/graphql/queries/sc-labs/home.graphql")
    mapped_content = map_home(aem_content)
    return mapped_content
```

### Adding a GraphQL query
GraphQL queries are located at ./lib/graphql/queries/[project name]/[your query name]

Import query from GraphQL client and provide query path as a parametert (AEM example below).
```
from lib.graphql.client import query
aem_content = query("./lib/graphql/queries/sc-labs/home.graphql")
```

### Adding a mapping
Create a new map in your projects /app/mapper file

Example
```
def map_home(aem_content):
    return {
        "title": aem_content["alphaDCHomeByPath"]["item"]["scTitleEn"]
    }
```