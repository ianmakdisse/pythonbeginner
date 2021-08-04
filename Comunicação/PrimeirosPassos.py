import socket
resultado = "SIM"
while (resultado=="SIM"):
    url=input("Digite uma url:")
    ip= socket.gethostbyname(url)
    print("o ip da url informada é igual a ip",ip)
    resultado=input("Digite SIM para continuar").upper()