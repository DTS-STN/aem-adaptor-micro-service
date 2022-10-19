from app.lib.graphql.client import query
from app.lib.mapper.sch_mapper import HomeContent, map_home


def get_home() -> HomeContent:
    aem_content = query("./app/lib/graphql/queries/sc-labs/home.graphql")
    mapped_content = map_home(aem_content)
    return mapped_content
