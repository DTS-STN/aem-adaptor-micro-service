from lib.graphql.client import query
from lib.mapper.sch_mapper import map_home
import os

def get_home():
    aem_content = query("./lib/graphql/queries/sc-labs/home.graphql")
    mapped_content = map_home(aem_content)
    return mapped_content