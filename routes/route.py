from fastapi import APIRouter
from models.vehiculos import Vehiculo
from config.database import collection_name
from schema.schema import list_serial
from bson import ObjectId

router = APIRouter()


# Get request method
@router.get("/get_vehiculos")
async def get_vehiculos():
    vehiculos = list_serial(collection_name.find())
    return vehiculos


# Post request method
@router.post("/")
async def post_vehiculo(vehiculo: Vehiculo):
    collection_name.insert_one(dict(vehiculo))


# PUT request method
@router.put("/{id}")
async def put_vehiculo(id: str,vehiculo: Vehiculo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(vehiculo)})


# DELETE request method
@router.delete("/{id}")
async def delete_vehiculo(id:str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})

    @router.put("/{license}")
    async def put_vehiculo(license: str, vehiculoUpdate: Vehiculo):
        vehiculos = list_serial(collection_name.find())
        for vehiculo in vehiculos:
            if vehiculo["license"] == license:
                get = vehiculo["id"]
                collection_name.find_one_and_update({"_id": ObjectId(get)}, {"$set": dict(vehiculoUpdate)})
        return {"Vehiculo No encontrado"}