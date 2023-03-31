from sqlmodel import SQLModel, Field

from typing import Optional


class Car(SQLModel, table=True):
	id: Optional[int] = Field(primary_key=True, default=None, index=True)
	brand: str
	model: str
	price: float
