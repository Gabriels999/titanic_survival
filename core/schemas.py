from pydantic import BaseModel


class TitanicPassenger(BaseModel):
    # id: int
    age: int
    fare: float
    sex: int
    sibsp: int
    parch: int
    pclass: int
    embarked: int
