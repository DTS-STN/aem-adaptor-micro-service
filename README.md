# aem-adaptor-micro-service
An AEM adaptor to query, map and cache AEM responses

## Required environment variables
AEM_GRAPHQL_ENDPOINT = "AEM's GraphQL endpoint"
APP_VERSION = "dts-aem-adaptor-ms/0.0.1"

## GraphQL query example
GraphQL queries are checked in under ./lib/graphql/queries/[project name]

Initialize a GraphQLWrapper object providing the endpoint and user-agent header (example below).
```
from lib.graphql.client import GraphQLWrapper
AEMClient = GraphQLWrapper(os.environ['AEM_GRAPHQL_ENDPOINT'], os.environ['APP_VERSION'])
AEMClient.query("./lib/graphql/queries/sc-labs/home.graphql")
```