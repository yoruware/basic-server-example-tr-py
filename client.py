import socket
host = "127.0.0.1" #Teknik açıdan 127.0.0.1, geri döngü amaçları için belirlenmiş Sınıf A ağına ait, yönlendirilemeyen bir adrestir. Kendi bilgisayarlarınla iletişim kurduğun anlamına gelir. "There is no place like 127.0.0.1" (yani evin burası)

port = 50001   #TCP ya da UDP kullanırken kendi port numaranı belirleyebilirsin, ama 0-1023 arası portlar "well-known ports" diye geçer (80 = http, 22 = ssh, 443 = https vs.), 1024-49151 arası registered portlardır yani bazı uygulamalar için ayrılmış olabilirler. Bu yüzden zaten kullanımda olan portlarla çakışma yaşamamak için yaklaşık 50.000den itibaren olan portları kullanabilirsin.

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
#socket nesnesini oluşturduk, AF_INET diyerek IPv4 kullanacağımızı belirttik, SOCK_STREAM ile TCP kullanacağımızı belirttik.

client_socket.connect((host,port))  #Bu kısımda parantezlere dikkat etmen önemli, çünkü connect() bizden bir tuple talep eder, biz de (host,port) yazarak bu tuple'ı tanımlıyoruz.

message = input(">> ")


while message.lower().strip()!="quit":   #lower() her şeyi küçük harfe çevirir, strip() baştaki ve sondaki boşlukları kaldırır.
    if(message!=""):
        client_socket.send(message.encode())
# encode() message'ı UTF-8 gibi bir formatla baytlara çevirir çünkü socket'ler sadece byte ile çalışır.
        data = client_socket.recv(1024).decode()
# en fazla 1024 bytelık mesaj alacağını ifade eder. sonra decode() ile alınan byte'ı string'e yani okunabilir hale çevirir.
        print("Response from server : "+str(data))
# server'dan gelen cevabı yazdırır.
    message = input(">> ")

client_socket.close()
