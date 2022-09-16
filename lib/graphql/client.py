from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

class GraphQLWrapper:
    def __init__(self, url, useragent):
        transport = RequestsHTTPTransport(
            url=url,
            verify=True,
            retries=3,
            headers={'user-agent': useragent},
        )
        self.gqlclient = Client(transport=transport, fetch_schema_from_transport=True)

    def load_query(self, path):
        with open(path) as f:
            return gql(f.read())

    def query(self, path):
        query = self.load_query(path)
        result = self.gqlclient.execute(query)
        print(result)
