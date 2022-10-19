import unittest

import pytest

from app.lib.content.sch_content import get_home


@unittest.skip("Issue with mocking")
def test_get_home(mocker):
    mocker.patch("app.lib.graphql.client.query")
    mocker.patch(
        "app.lib.mapper.sch_mapper.map_home",
        return_value={"title": "Search for benefits and services"},
    )
    home_content = get_home()
    assert home_content == {"title": "Search for benefits and services"}
