from typing import Any

class HomeContent():
    title: str

def map_home(aem_content: Any) -> HomeContent:
    homeContent = HomeContent()
    homeContent.title = aem_content["alphaDCHomeByPath"]["item"]["scTitleEn"]
    return homeContent
