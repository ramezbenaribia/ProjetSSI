from socket import *

# Créer une Socket

tcp_server = socket(AF_INET, SOCK_STREAM)

# BINDip,port

# Ici.ipNatif par défaut

address = ('192.168.1.17', 8000)

tcp_server.bind(address)

# Démarrer la connexion passive

# Combien de clients peuvent se connecter

tcp_server.listen(128)

# UtilisersocketLa propriété par défaut de la socket créée est active

# UtiliserlistenPour le rendre passif,Pour recevoir les liens de quelqu'un d'autre

# Créer une réception

# S'il y a un nouveau client pour lier le serveur,Il en résulte une nouvelle socket dédiée à ce client

client_socket, clientAddr = tcp_server.accept()


# Recevoir les données envoyées par l'autre partie

# Réception1024Octets,Ici.recvCe n'est plus un Tuple reçu,La différenceUDP
from_client_msg = client_socket.recv(1024)

print("Données reçues：", from_client_msg.encode("gbk"))

# Envoyer les données au client

send_data = client_socket.send(
    "Bonjour, client.,Reçu du côté du serveur,Numéro public【PythonLes chercheurs】".encode("gbk"))

# Fermez la prise

# Fermez la prise qui dessert ce client,Ça veut dire ne plus pouvoir servir ce client

# Si le service est nécessaire,Je ne peux que me reconnecter.

client_socket.close()
