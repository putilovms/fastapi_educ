from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel, SHotels

router = APIRouter(
    prefix="/hotels",
    tags=['Hotels and Rooms']
)


@router.get("/location/{location}")
@cache(expire=20)
async def get_hotels_by_location(
    location: str,
    date_from: date,
    date_to: date
) -> list[SHotels]:
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    # await asyncio.sleep(3)
    # ta = TypeAdapter(list[SHotels])
    # hotels = ta.validate_python(hotels)
    return hotels


@router.get("/id/{id}")
async def get_hotel(id: int) -> SHotel:
    hotel = await HotelDAO.find_by_id(id)
    # return SHotel.model_validate(hotel).model_dump_json()
    return hotel


@router.get("/all")
async def get_hotels_all() -> list[SHotel]:
    hotels = await HotelDAO._find_all()
    return hotels
