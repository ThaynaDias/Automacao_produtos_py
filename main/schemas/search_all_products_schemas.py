search_all_products_schemas = {
  "type": "object",
  "properties": {
    "loja": {
      "type": "string",
      "minLength": 1
    },
    "produtos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "marca": {
            "type": "string",
            "minLength": 1
          },
          "nome": {
            "type": "string",
            "minLength": 1
          },
          "preco": {
            "type": "number"
          }
        },
        "required": ["id", "marca", "nome", "preco"]
      }
    }
  },
  "required": ["loja", "produtos"]
}