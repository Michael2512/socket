#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224 #comunicare sulla stessa porta

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ")  #chiedere di inserire i dati
    except EOFError:
        print("\nOkay. Exit") #se ci sono errori uscire
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!")  #se non ci sono dati dire quella frase
        continue
    if dati == '0':
        print("Chiudo la connessione con il server!") #se i dati sono 0 chiudere la comunicazioni
        break
    
    dati = dati.encode()  #dato che tra le socket le stringhe ecc vengono codificate in nyte server per decodificarli

    sock_service.send(dati) #mandare i dati

    dati = sock_service.recv(2048)

    if not dati:
        print("Server non risponde. Exit")
        break
    
    dati = dati.decode() #decodificare i dati

    print("Ricevuto dal server:")  #output ricevuto dal server
    print(dati + '\n') 

sock_service.close()