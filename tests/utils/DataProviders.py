import csv
from pathlib import Path

dataFile = ("providersDP.csv")
url_data_provider = "resources"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(url_data_provider).joinpath(dataFile)

def get_data():
    with open(DATA_FILE,"r") as f:
        reader = csv.reader(f)
        next(reader) #pular primeira linha do arquivo (cabeçalho)
        data = [tuple(row) for row in reader]
    return data