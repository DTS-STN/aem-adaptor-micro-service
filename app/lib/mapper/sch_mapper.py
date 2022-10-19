from typing import Any, List

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    link: str
    icon: str


class CardList(BaseModel):
    title: str
    tasks: List[Task]


class Card(BaseModel):
    id: str
    title: str
    lists: List[CardList]


class ExitBeta(BaseModel):
    title: str
    link: str


class HomeContent(BaseModel):
    title: str
    cards: List[Card]
    exitBeta: ExitBeta


def map_home(aem_content: Any) -> HomeContent:
    cards: list[Card] = []
    exitBeta: ExitBeta = ExitBeta(**{"title": "Not found", "link": "Not found"})

    for element in aem_content["schPagev1ByPath"]["item"]["scFragments"]:
        if element["scId"] == "dashboard-cards":
            cards = map_dashboard_cards(element["scItems"])
        if element["scId"] == "exit-beta-version":
            exitBeta = map_exit_beta(element)

    homeContent = HomeContent(
        **{
            "title": aem_content["schPagev1ByPath"]["item"]["scTitleEn"],
            "cards": cards,
            "exitBeta": exitBeta,
        }
    )

    return homeContent


def map_dashboard_cards(aem_cards: Any) -> List[Card]:
    cards: List[Card] = []
    for card in aem_cards:
        card_lists: List[CardList] = map_card_lists(card["schLists"])
        cards.append(
            Card(
                **{"id": card["scId"], "title": card["scTitleEn"], "lists": card_lists}
            )
        )
    return cards


def map_card_lists(aem_card_lists: Any) -> List[CardList]:
    card_lists: List[CardList] = []
    for card_list in aem_card_lists:
        tasks: List[Task] = map_list_tasks(card_list["scItems"])
        card_lists.append(CardList(**{"title": card_list["scTitleEn"], "tasks": tasks}))
    return card_lists


def map_list_tasks(aem_tasks: Any) -> List[Task]:
    tasks: List[Task] = []
    for task in aem_tasks:
        tasks.append(
            Task(
                **{
                    "title": task["scTitleEn"],
                    "link": task["scDestinationURLEn"],
                    "icon": task["scIconCSS"],
                }
            )
        )
    return tasks


def map_exit_beta(aem_exit_beta: Any) -> ExitBeta:
    return ExitBeta(
        **{
            "title": aem_exit_beta["scTitleEn"],
            "link": aem_exit_beta["scDestinationURLEn"],
        }
    )
