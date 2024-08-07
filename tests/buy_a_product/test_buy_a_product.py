import pytest
from main.routes.buy_a_product.post_buy_a_product import post_but_a_product_route
from main.schemas.buy_a_product_schemas import buy_a_product_schemas
from jsonschema import ValidationError, validate

@pytest.mark.sanity
def test_success_buy_a_product():
    response = post_but_a_product_route("Thayná Dias", "12345678910", "1", "4500", "teste@gmail.com")

    # Verificar se a resposta não é None
    assert response is not None, "The response is None. Check if the request was successful."

    # Verificar o código de status diretamente no objeto Response
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

    # Verificar o corpo da resposta
    expected_body = {
        "produto": {
            "id": 1,
            "marca": "Samsung",
            "nome": "TV Smart 4K",
            "preco": 4500
        },
        "message": "Compra realizada com sucesso"
    }

    # Decodificar o corpo da resposta JSON
    response_json = response.json()

    # Verificar o corpo da resposta contra o formato esperado
    assert response_json == expected_body, f"Expected body {expected_body}, but got {response_json}"

    # Validar o JSON da resposta contra o schema, se aplicável
    try:
        validate(instance=response_json, schema=buy_a_product_schemas)
    except ValidationError as e:
        pytest.fail(f"Response does not match schema: {e}")
    except ValueError as e:
        pytest.fail(f"Failed to decode JSON response: {e}")