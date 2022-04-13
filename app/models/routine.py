from datetime import date, datetime, time
from lib2to3.pytree import Base
from pydantic import BaseModel, Field
from typing import Optional


class Machine(BaseModel):
    sub: Optional[int] = None
    name: str = Field(...)
    target_day: str = Field(...)
    set_date: datetime = Field(...)
    last_used: Optional[datetime] = None


class Workout(BaseModel):
    sub: Optional[int] = None
    machine_id: str = Field(...)
    last_weight: Optional[int] = None
    reps: Optional[str] = None
    time: Optional[time] = None
    date: Optional[datetime] = None


class Routine(BaseModel):
    day: str = Field()


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
