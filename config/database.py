from pymongo import MongoClient

client = MongoClient("mongodb+srv://jmgomezc14:estoEsTesting@compraventadb.qgdua4j.mongodb.net/?retryWrites=true&w=majority&appName=compraVentaDB")

db = client.vehiculos

collection_name = db["vehiculos"]