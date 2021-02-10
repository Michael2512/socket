#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224  #server per far comunicare il socket ed il client sulla stessa porta 

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client))   #vedere se la connessione è avvenuta 
    print("\nAspetto di ricevere i dati ")   #chiedere di inserire i dati
    contConn=0  #contatore inizializzato a 0
    while True:
        dati = sock_service.recv(2048)  #numero massimo di caratteri
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")  #se non ci sono i dati finire il client
            break
        
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)
        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client))  #se i dati sono 0 chiudere la connessione tra client e server
            break
        dati = "Risposta a : " + str(addr_client) + ". Il valore del contatore è : " + str(contConn)  #risposta e valore contatore

        dati = dati.encode() #dato che tra le socket le stringhe ecc vengono codificate in nyte server per decodificarli

        sock_service.send(dati) #mandare i dati al client

    sock_service.close()