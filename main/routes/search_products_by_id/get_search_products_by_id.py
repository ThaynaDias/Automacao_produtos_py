import requests

ROUTE = "https://api-desafio-qa.onrender.com/produtos/"

def get_search_products_by_id_route(id):
    header = {"accept":"*/*", "Content-Type":"application/json"}
    params = {"id": id}

    try:
        response = requests.get(ROUTE, params=params, headers=header, timeout=30)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None 