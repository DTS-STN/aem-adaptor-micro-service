import pytest
from app.lib.graphql import client
from gql import gql
import graphql

def test_load_query(mocker):
    query = client.load_query('./app/lib/graphql/queries/sc-labs/home.graphql')
    assert type(query) is graphql.language.ast.DocumentNode


def test_query(mocker):
    mocker.patch(
        'app.lib.graphql.client.gqlclient.execute',
        return_value = {'title': 'Search for benefits and services'}
    )
    response = client.query('./app/lib/graphql/queries/sc-labs/home.graphql')
    assert response == {'title': 'Search for benefits and services'}