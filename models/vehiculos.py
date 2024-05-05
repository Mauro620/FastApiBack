import datetime
from pydantic import BaseModel

class Vehiculo(BaseModel):
    status: str
    license: str
    type: str
    brand: str
    model: str
    color: str
    year: str
    cc: str
    initial_price: float
    shipper: str = None
    kms: str
    sell_price: float = None
    is_offer: bool = False
    sell_date: str = None
    register_date: str = None
    seller: str = None

