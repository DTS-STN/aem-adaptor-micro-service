from fastapi import APIRouter
from lib.content import sch_content

router = APIRouter()

@router.get("/sch/home")
async def read_root():
    return sch_content.get_home()
