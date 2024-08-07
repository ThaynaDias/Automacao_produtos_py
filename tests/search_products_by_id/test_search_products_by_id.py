import pytest
from main.routes.search_products_by_id.get_search_products_by_id import get_search_products_by_id_route
from main.schemas.search_products_by_id_schemas import search_products_by_id_schemas
from jsonschema import ValidationError,validate

@pytest.mark.sanity
def test_sucess_search_products_by_id():
    response = get_search_products_by_id_route("2")

    assert response is not None, "A resposta é None. Verifique se a solicitação foi bem-sucedida."
    assert response.status_code == 200, f"Esperado código de status 200, mas obtido {response.status_code}"

    response_json = response.json()

    # Verificar o nome da loja
    assert "loja" in response_json, "O JSON da resposta não contém a chave 'loja'."
    assert response_json["loja"] == "Loja QA Tester", f"Esperado 'Loja QA Tester', mas obtido {response_json['loja']}"

    # Verificar os detalhes do produto
    expected_product = {
        "id": 1,
        "nome": "TV Smart 4K",
        "marca": "Samsung",
        "preco": 4500
    }

    produtos = response_json.get("produtos", [])
    produto_encontrado = any(produto == expected_product for produto in produtos)
    
    assert produto_encontrado, f"Produto esperado {expected_product} não encontrado na resposta."
