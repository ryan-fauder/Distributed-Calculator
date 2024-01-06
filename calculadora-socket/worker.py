import threading
from communication import Communication
import json
from message import Message
from calculator import Calculator
class Worker(threading.Thread):
    def __init__(self, client_socket, client_address):
        super().__init__()
        self.client_socket = client_socket
        self.client_address = client_address
        self.connection = Communication(client_socket)
    def run(self):
        print(f"[*] Conexão aceita de {self.client_address[0]}:{self.client_address[1]}")
        message = Communication.receive(self.client_socket)
        self.handle(message)

        self.client_socket.close()
        print(f"[*] Conexão encerrada com {self.client_address[0]}:{self.client_address[1]}")

    def handle(self, request: Message):
        data = json.loads(request.data)
        operation = data["operation"]
        first = int(data["first"])
        second = int(data["second"])
        result = 0
        try:
            if(operation == 'add'):
                result = Calculator.add(first, second)
            elif(operation == 'sub'):
                result = Calculator.sub(first, second)
            elif(operation == 'div'):
                result = Calculator.div(first, second)
            elif(operation == 'mul'):
                result = Calculator.mul(first, second)
            else:
                raise Exception('Operação inválida')
            message = Message('response', 'int', str(result), len(str(result)))
            self.connection.send(message)
        except:
            self.connection.send_error('Operação inválida')
