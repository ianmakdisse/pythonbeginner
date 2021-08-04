from socket import *
servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_STREAM) #AF_INET, o que significa que iremos utilizar a identificação do emissor/receptor do(s) pacote(s) via DNS ou número IP (poderíamos utilizar a constante AF_UNIX, o que mudaria a forma de identificar a origem/destino do(s) pacote(s)). Já o segundo parâmetro refere-se ao transporte desse pacote, que pode ser SOCK_STREAM, que representa o protocolo TCP (o que nós optamos) ou SOCK_DGRAM, que representa o protocolo de transporte UDP.
obj_socket.bind((servidor,porta)) # assosiação entre o servidor e a porta
obj_socket.listen(2) #eu limito a operação para apenas dois clientes
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", str(msg_recebida))
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8')
        con.send(msg_enviada)
        break
    con.close()