import pytest
from app.lib.mapper.sch_mapper import map_home

def test_map_home():
    aem_content = {'alphaDCHomeByPath': {'item': {'_path': '/content/dam/decd-endc/content-fragments/alpha/dev/components/home/search-for-benefits-and-services', 'scTitleEn': 'Search for benefits and services'}}}
    mapped_content = map_home(aem_content)
    assert mapped_content == {'title': 'Search for benefits and services'}