"""
Cliente que manda el archivo (Subida)
"""
import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4

def send_file(filename, host, port):
    #Obtener el tamano del archivo
    filesize = os.path.getsize(filename)
    #Crear el socker client
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print ("[+] Connected.")

    #Enviar el filename y el filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    #Empezar a enviar el archivo
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit = "B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
       	while True:
        	#Leer los bytes desde el archivo
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                   #Tansferencia de archivo esta hecha
                   break
                #Usamos sendall para asegurarnos de la transmicion
                s.sendall(bytes_read)
                #Actualizamos la barra de progreso
                progress.update(len(bytes_read))

    #Cerramos el socket
    s.close()

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Receiver")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address of the receiver")
    parser.add_argument("-p", "--port", help="Port to use, default is 5001", type=int, default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    send_file(filename, host, port)
