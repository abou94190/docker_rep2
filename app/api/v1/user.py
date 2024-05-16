from fastapi import APIRouter

router = APIRouter()


@router.get("/user/")
async def read_items():
    return [{"all": "BTC"}]
