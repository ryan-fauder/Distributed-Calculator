import socket
from worker import Worker
import environment
import os
class Dispatcher:
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        while True:
            client, addr = self.server_socket.accept()
            worker = Worker(client, addr)
            worker.start()

def main():
    host = os.environ['server_host']
    port = os.environ['server_port']

    dispatcher = Dispatcher(host, port)
    dispatcher.listen()

if __name__ == "__main__":
    main()