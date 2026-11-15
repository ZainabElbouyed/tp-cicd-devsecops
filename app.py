from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # On récupère l'ID du conteneur pour prouver que ça tourne dans Docker
    hostname = socket.gethostname()
    user = os.getenv('USER', 'inconnu')
    return f"<h1>Hello depuis mon API Flask !</h1><p>Conteneur : {hostname}</p><p>Utilisateur : {user}</p>"

if __name__ == '__main__':
    # Écoute sur 0.0.0.0 pour être accessible depuis l'extérieur du conteneur
    app.run(host='0.0.0.0', port=8080)