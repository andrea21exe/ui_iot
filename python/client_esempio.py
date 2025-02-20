# %%
import requests

url = "http://127.0.0.1:9998"

# Dati di esempio con coordinate
data = {
    "latitudine": [
        45.4642, 45.4643, 45.4645, 45.4647,  # Milano
        45.0703, 7.6869,  # Torino
        45.4384, 10.9916,  # Verona
        44.4949, 11.3426,  # Bologna
        43.7696, 11.2558,  # Firenze
        41.9028, 12.4964,  # Roma
        40.8518, 14.2681,  # Napoli
        38.1157, 13.3615   # Palermo
    ],
    "longitudine": [
        9.1900, 9.1902, 9.1905, 9.1907,  # Milano
        7.6869, 7.6870,  # Torino
        10.9916, 10.9918,  # Verona
        11.3426, 11.3428,  # Bologna
        11.2558, 11.2560,  # Firenze
        12.4964, 12.4966,  # Roma
        14.2681, 14.2683,  # Napoli
        13.3615, 13.3617   # Palermo
    ],
    "co2_media": [412.5] * 16,  # Valore costante per tutte le coordinate
    "accelerazione_media": [2.3] * 16,  # Valore costante per tutte le coordinate
    "tempo": ["2025-02-20T14:30:00Z"] * 16  # Valore costante per tutte le coordinate
}

response = requests.post(url, json=data)
print(response.json())
