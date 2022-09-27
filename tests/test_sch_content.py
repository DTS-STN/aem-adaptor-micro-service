import pytest
from lib.content.sch_content import get_home

def test_get_home(mocker):
    mocker.patch(
        'lib.graphql.client.query'
    )
    mocker.patch(
        'lib.mapper.sch_mapper.map_home',
        return_value={'title': 'Search for benefits and services'}
    )
    home_content = get_home()
    assert home_content == {'title': 'Search for benefits and services'}
