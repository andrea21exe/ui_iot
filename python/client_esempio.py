# %%
import requests
import numpy as np

url = "http://127.0.0.1:9999"

# Coordinate di Leonforte e Agira
leonforte = (37.64197, 14.39766)
agira = (37.6558, 14.51972)

def generate_path(start, end, num_points=100):
    latitudes = []
    longitudes = []
    
    # Interpolazione tra il punto di partenza e quello di arrivo
    for t in np.linspace(0, 1, num_points):
        lat = start[0] + t * (end[0] - start[0])
        lon = start[1] + t * (end[1] - start[1])
        latitudes.append(lat)
        longitudes.append(lon)
    
    return latitudes, longitudes

# Esempio json
data = {
    "latitudine": generate_path(leonforte, agira)[0],
    "longitudine": generate_path(leonforte, agira)[1],
    "co2_media": 4839.5,  
    "accelerazione_media": 2.3,  
    "tempo": "2025-02-20T14:30:00Z"
}

response = requests.post(url, json=data)
print(response.json())
