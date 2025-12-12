import socket

# Define uma função (scan_port) que encapsula a lógica do scanner. Define os seguintes parâmetros: host, star_port, end_port, timeout que serão usados ao longo do código
def scan_port(host, start_port, end_port, timeout):
    # Inicia um loop que itera por cada número de porta no intervalo inclusivo entre start_port e end_port. +1 garante que o end_port seja incluido, pois gera a sequência exclusiva do limite superior
    for port in range(start_port, end_port + 1):
        # Cria um novo objeto socket TCP/IPV4 e atribui a variável setSocket
        setSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Configura o tempo máximo (em segundos) antes de lançar um erro de timeout. Sem o timeout, uma tentativa de conexão para uma porta filtrada ou sem resposta poderia travar indefinidamente, tornando a varredura impraticável.
        setSocket.settimeout(timeout)

        # O Try executa uma operação que pode falhar, porém sem quebrar o programa.
        try:
            # Essa linha tenta estabelecer uma conexão TCP com uma porta específica do host.
            setSocket.connect((host, port))
            print(f"Port {port} is OPEN")
        # O Except captura qualquer conexão gerada dentro do Try. Quando a conexão falha, o socket lança uma exceção (socket.error) e o except intercepta e permite que trate esse erro sem encerrar o programa.
        except:
            print(f"Port {port} is CLOSED")
        # O Finally sempre executa, independentemente de ter ocorrido erro ou sucesso. O objetivo é garantir que o socket seja fechado, impedindo vazamento de recursos, consumo desnecessário de file descriptors, travamentos e alcance do limite do sistema para sockets abertos.
        finally:
            setSocket.close()

# O seguinte If não é o mesmo de quando falamos de if e else. Esse if é um ponto de entrada que executa o arquivo diretamente, uma condição que, quando verdadeira, executa o código dentro dela e, quando falso, não executa.
if __name__ == "__main__":
    scan_port("x.com", 70, 90, 1)
    # Podemos colocar qualquer domínio dentro das aspas para verificar as portas abertas.