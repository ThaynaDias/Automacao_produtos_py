import requests

ROUTE = "https://api-desafio-qa.onrender.com/produtos"

def get_search_all_products_route():
    header = {
        "accept": "*/*",
        "content-Type": "application/json"
    }

    try: 
        response = requests.get(ROUTE, headers=header, timeout=30)
        response.raise_for_status()
        return response
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None 