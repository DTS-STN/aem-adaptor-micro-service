from fastapi import APIRouter

from app.lib.content.sch_content import get_home
from app.lib.mapper.sch_mapper import HomeContent

router = APIRouter(prefix="/sch")


@router.get("/home")
async def read_sch_get_home() -> HomeContent:
    return get_home()
