import socket


class Comunicador:
    HOST = '127.0.0.1'
    PORT = 65432

    @staticmethod
    def receba_mensagem(host='', port=0) -> str:
        if host == '':
            host = Comunicador.HOST
        if port == 0:
            port = Comunicador.PORT
        mensagem = ''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Conectado por ', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    mensagem = repr(data)
        return Comunicador.formata_mensagem(str(mensagem))

    @staticmethod
    def envie_mensagem(mensagem:str, host='', port=0) -> None:
        if host == '':
            host = Comunicador.HOST
        if port == 0:
            port = Comunicador.PORT
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(bytes(mensagem, encoding='utf8'))

    @staticmethod
    def formata_mensagem(mensagem: str) -> str:
        return mensagem.split('\'')[1]