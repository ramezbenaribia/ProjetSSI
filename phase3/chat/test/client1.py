from socket import *

# 1.Créer une Socket

tcp_socket = socket(AF_INET, SOCK_STREAM)

# 2.Préparez - vous à vous connecter au serveur,Établir une connexion


address = ('192.168.1.17', 8000)
# Connexion au serveur,Établir une connexion,L'argument est sous forme de Tuple
tcp_socket.connect(address)

# Préparation des données à transmettre

send_data = "C'est aujourd'hui.2021Année08Mois29Jour,Frère Chen a envoyé des données au serveur"

tcp_socket.send(send_data.encode("gbk"))

# Recevoir des données du serveur

# Regarde ça.1024byte,La taille est fixée en fonction des besoins

from_server_msg = tcp_socket.recv(1024)

# Plus.decode("gbk")Ça résout le désordre.

print(from_server_msg.decode("gbk"))

# Fermer la connexion

tcp_socket.close()
