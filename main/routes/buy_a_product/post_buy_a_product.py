import requests

ROUTE = "https://api-desafio-qa.onrender.com/produtos"

def post_but_a_product_route(nome, cpf, id_produto, valor_na_carteira, send_email):
    header = {"accept": "*/*", "Content-Type": "application/json"}
    payload = {
        "nome": nome,
        "cpf": cpf,
        "id_produto": id_produto,
        "valor_na_carteira": valor_na_carteira,
        "send_email": send_email
    }

    try:
        response = requests.post(ROUTE, json=payload, headers=header, timeout=30)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        return response  # Retorna o objeto de resposta completo
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None  # Retorna None em caso de erro
