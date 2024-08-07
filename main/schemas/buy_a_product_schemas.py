# main/schemas/buy_a_product_schemas.py

buy_a_product_schemas = {
    "type": "object",
    "properties": {
        "produto": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "marca": {"type": "string"},
                "nome": {"type": "string"},
                "preco": {"type": "number"}
            },
            "required": ["id", "marca", "nome", "preco"]
        },
        "message": {"type": "string"}
    },
    "required": ["produto", "message"]
}
