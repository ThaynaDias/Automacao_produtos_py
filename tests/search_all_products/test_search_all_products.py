import pytest 
from main.routes.search_all_products.get_search_all_products import get_search_all_products_route
from main.schemas.search_all_products_schemas import search_all_products_schemas
from jsonschema import ValidationError, validate

@pytest.mark.sanity
def test_sucess_search_all_products():
    response = get_search_all_products_route()

    assert response is not None, "The response is None. Check if the request was successful"
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    except_body = {

  "loja": "Loja QA Tester",
  "produtos": [
    {
      "id": 1,
      "marca": "Samsung",
      "nome": "TV Smart 4K",
      "preco": 4500
    },
    {
      "id": 2,
      "marca": "LG",
      "nome": "OLED 55' 4K",
      "preco": 6200
    },
    {
      "id": 3,
      "marca": "Sony",
      "nome": "QLED 8K",
      "preco": 13000
    },
    {
      "id": 4,
      "marca": "Apple",
      "nome": "iPhone 13 Pro Max",
      "preco": 7500
    },
    {
      "id": 5,
      "marca": "Apple",
      "nome": "iPhone 12",
      "preco": 6000
    },
    {
      "id": 6,
      "marca": "Apple",
      "nome": "iPhone 13",
      "preco": 6800
    },
    {
      "id": 7,
      "marca": "Apple",
      "nome": "MacBook Pro 14'",
      "preco": 22000
    },
    {
      "id": 8,
      "marca": "Apple",
      "nome": "MacBook Air",
      "preco": 12000
    },
    {
      "id": 9,
      "marca": "Apple",
      "nome": "MacBook Pro 16'",
      "preco": 28000
    },
    {
      "id": 10,
      "marca": "Samsung",
      "nome": "Galaxy Tab S7",
      "preco": 4500
    },
    {
      "id": 11,
      "marca": "Apple",
      "nome": "iPad Pro",
      "preco": 9500
    },
    {
      "id": 12,
      "marca": "Microsoft",
      "nome": "Surface Pro",
      "preco": 8900
    },
    {
      "id": 13,
      "marca": "JBL",
      "nome": "JBL Flip 5",
      "preco": 900
    },
    {
      "id": 14,
      "marca": "JBL",
      "nome": "JBL Boombox",
      "preco": 2500
    },
    {
      "id": 15,
      "marca": "JBL",
      "nome": "JBL Charge 4",
      "preco": 1100
    },
    {
      "id": 16,
      "marca": "Oculus",
      "nome": "Oculus Quest 2",
      "preco": 3000
    },
    {
      "id": 17,
      "marca": "Oculus",
      "nome": "Oculus Rift S",
      "preco": 3500
    },
    {
      "id": 18,
      "marca": "HTC",
      "nome": "HTC Vive Pro",
      "preco": 6000
    },
    {
      "id": 19,
      "marca": "Sony",
      "nome": "Sony PlayStation VR",
      "preco": 2500
    },
    {
      "id": 20,
      "marca": "Samsung",
      "nome": "Samsung Gear VR",
      "preco": 1000
    }]

}
    
    response_json = response.json()

    assert response_json == except_body, f"Expected body {expected_body}, but got {response_json}"

    try:
        validate(instance=response_json, schema=search_all_products_schemas)
    except ValidationError as e:
        pytest.fail(f"Response does not match schema: {e}")
    except ValueError as e:
        pytest.fail(f"Failed to decode JSON response: {e}")
