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

    # Calcolare i valori minimi e massimi per centrare la mappa
    lat_mean = data['Latitudine'].mean()
    lon_mean = data['Longitudine'].mean()

    # Creare la mappa con scatter_mapbox
    fig = px.scatter_mapbox(data,
                             lat='Latitudine',
                             lon='Longitudine',
                             title='Percorso sulla mappa',
                             color='index',
                             hover_name=data.index)  

    
    # Centra la mappa
    fig.update_layout(
        mapbox=dict(
            center=dict(lat=lat_mean, lon=lon_mean),  
            zoom=10 
        )
    )
    # Aggiorna lo stile della mappa
    fig.update_layout(mapbox_style="open-street-map")

    fig.show()

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            # Stampa i dati ricevuti
            data = json.loads(post_data.decode('utf-8'))
            print("Ricevuto JSON:", json.dumps(data, indent=2))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
            # Mostra la mappa
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
