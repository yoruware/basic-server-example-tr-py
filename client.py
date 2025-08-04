import socket
host = "127.0.0.1"
port = 50001

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#socket nesnesini oluşturduk, AF_INET diyerek IPv4 kullanacağımızı belirttik, SOCK_STREAM ile TCP kullanacağımızı belirttik.

client_socket.connect((host,port))

message = input(">> ")

#lower() her şeyi küçük harfe çevirir, strip() baştaki ve sondaki boşlukları kaldırır

while message.lower().strip()!="quit":
    if(message!=""):
        client_socket.send(message.encode())
#encode() message'ı UTF-8 gibi bir formatla baytlara çevirir çünkü socket'ler sadece byte ile çalışır
        data = client_socket.recv(1024).decode()
# en fazla 1024 bytelık mesaj alacağını ifade eder. sonra decode() ile alınan byte'ı string'e yani readable hale çevirir.
        print("Response from server : "+str(data))
# server'dan gelen cevabı yazdırır.
    message = input(">> ")

client_socket.close()
