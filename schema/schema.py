def individual_serial(vehiculo) -> dict:
    return {
        "id": str(vehiculo["_id"]),
        "status": vehiculo["status"],
        "license": vehiculo["license"],
        "type": vehiculo["type"],
        "brand": vehiculo["brand"],
        "model": vehiculo["model"],
        "color": vehiculo["color"],
        "year": vehiculo["year"],
        "cc": vehiculo["cc"],
        "initial_price": vehiculo["initial_price"],
        "shipper": vehiculo["shipper"],
        "kms": vehiculo["kms"],
        "sell_price": vehiculo["sell_price"],
        "is_offer": vehiculo["is_offer"],
        "sell_date": vehiculo["sell_date"],
        "register_date": vehiculo["register_date"],
        "seller": vehiculo["seller"],
    }

def list_serial(vehiculos) -> list:
    return[individual_serial(vehiculo) for vehiculo in vehiculos ]