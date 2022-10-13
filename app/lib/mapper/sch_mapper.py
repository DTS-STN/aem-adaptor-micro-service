from typing import Any
from pydantic import BaseModel

class HomeContent(BaseModel):
    title: str

def map_home(aem_content: Any) -> HomeContent:
    homeContent = HomeContent(**{"title": aem_content["alphaDCHomeByPath"]["item"]["scTitleEn"]})
    return homeContent
