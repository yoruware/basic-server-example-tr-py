import socket
import subprocess #clientın talep ettiği komutları çalıştırmak için

host = "127.0.0.1"
port = 50001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_TEAM)
server_socket.bind((host,port))
server_socket.listen()  #önce sus bi dinle gelen mesajı al diyor

conn, addr = server_socket.accept()
print("connected from : "+str(addr))

while True:
    data = conn.recv(1024).decode()
    print(data)

    result = subprocess.run(data, stdout=subprocess.PIPE, shell=True)  
    # ! subprocess.run() cmd çalıştırıyor.
    # stdout=subprocess.PIPE >> komutun çıktısını al, terminale yazdırma

    # shell=True >>  komutları kabuk (shell) üzerinden çalıştır 

    #bu bir integer değil aslında bir sabittir (değeri: -1), sistemle alakalı bi anlamı var. çıktıyı yakalamamı sağlar. integera çevirmez, sadece stdout'u bir boruya yönlendirir.

    if(result.stdout.decode()!=""):
        response_data = result.stdout #çıktı
    else:
        response_data = ("Komut Calıstırıldı").encode()




    response_data = "Mesaj Alindi"
    conn.send(response_data.encode())
conn.close()
