search_products_by_id_schemas = {
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "nome": {
      "type": "string",
      "minLength": 1
    },
    "marca": {
      "type": "string",
      "minLength": 1
    },
    "preco": {
      "type": "number"
    }
  },
  "required": ["id", "nome", "marca", "preco"]
}
