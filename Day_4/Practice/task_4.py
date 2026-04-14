# На вход подается словарь order_data. 
# Напишите модели Pydantic для этого словаря, учитывая список элементов. 
# Сериализуйте и десериализуйте словарь.

from pydantic import BaseModel

order_data = {
    "items": [
        {"name": "Яблоко", "price": 1.5}, 
        {"name": "Банан", "price": 2.0}
    ]
}


class Item(BaseModel):
    name: str
    price: float


class Order(BaseModel):
    items: list


new_order = Order(**order_data)
new_order_json = new_order.model_dump_json(indent=4)
print(new_order_json)

order = Order.model_validate_json(new_order_json)
print(order)
print(order.items[1]["name"])