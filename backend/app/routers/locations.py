from fastapi import APIRouter
from app.data.locations import locations


router = APIRouter()


@router.get("/locations")
def get_locations():

    return locations