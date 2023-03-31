from typing import Optional, List
from sqlmodel import select
from database import get_session
from models import Car


def add_car_to_database(
        brand: str,
        model: str,
        price: float
) -> bool:
    with get_session() as session:
        car = Car(**locals())
        session.add(car)
        session.commit()    
    return True
