from fastapi import APIRouter
from app.lib.content import sch_content

router = APIRouter(prefix="/sch")

@router.get("/home")
async def read_sch_get_home():
    return sch_content.get_home()
