# %%
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import plotly.express as px
import pandas as pd

def show_map(lat: list, lon: list):
    data = pd.DataFrame({
        'Latitudine': lat,
        'Longitudine': lon
    })
    data['index'] = data.index

    # Calcolare i valori minimi e massimi per il centro e il livello di zoom
    lat_min = data['Latitudine'].min()
    lat_max = data['Latitudine'].max()
    lon_min = data['Longitudine'].min()
    lon_max = data['Longitudine'].max()

    # Calcolare il centro della mappa
    center_lat = (lat_min + lat_max) / 2
    center_lon = (lon_min + lon_max) / 2

    # Impostare il range di zoom
    zoom = 13  # Puoi regolare questo valore per il livello di zoom desiderato

    # Creare la mappa con scatter_mapbox
    fig = px.scatter_mapbox(data,
                             lat='Latitudine',
                             lon='Longitudine',
                             title='Percorso sulla mappa',
                             color='index',
                             hover_name=data.index)  # Opzionale, mostra l'indice

    fig.update_layout(mapbox_style="open-street-map")

    # Zoom sulla mappa e impostazione del centro
    fig.update_layout(
        mapbox=dict(
            center=dict(lat=center_lat, lon=center_lon),  
            zoom=zoom 
        )
    )

    fig.show()

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            print("Ricevuto JSON:", json.dumps(data, indent=2))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
            show_map(data['latitudine'], data['longitudine'])
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": "Invalid JSON"}).encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 9998)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server in ascolto sulla porta 9999...")
    httpd.serve_forever()




# %%
