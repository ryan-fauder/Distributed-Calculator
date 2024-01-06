import socket
from message import Message
from protocol import Protocol
class Communication:
    def __init__(self, socket: socket.socket) -> None:
        self.socket = socket
    def send(self, message: Message):
        data = Protocol.marshalMessage(message)
        self.socket.send(b'START')
        self.socket.sendall(data)
        self.socket.send(b'END')
    def send_error(self, error: str):
        message = Message('Error', 'str', error, len(error))
        self.send(message)
    def receive(connection: socket.socket) -> Message:
        message: bytes = b''
        start = connection.recv(5)
        if(start == b'START'):
            while True:
                data: bytes = connection.recv(1024)
                if not data:
                    break
                if data.find(b'END'):
                    message += data.removesuffix(b'END')
                    break
                message += data
        return Protocol.unmarshalMessage(message)