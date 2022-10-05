import os

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport(
    url=os.environ["AEM_GRAPHQL_ENDPOINT"],
    verify=True,
    retries=3,
    headers={"user-agent": os.environ["APP_VERSION"]},
)

gqlclient = Client(transport=transport, fetch_schema_from_transport=True)


def load_query(path):
    with open(path) as f:
        return gql(f.read())


def query(path):
    query = load_query(path)
    response = gqlclient.execute(query)
    return response
