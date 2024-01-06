import environment
import os
import socket
from communication import Communication
from message import Message
import json

def calculate(operation, first, second):
    host = os.environ['server_host']
    port = int(os.environ['server_port'])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    message = createCalculateMessage(operation, first, second)
    connection = Communication(client)
    connection.send(message)
    response = Communication.receive(client)
    value = int(response.data)
    client.close()
    return value

def createCalculateMessage(operation, first, second):
    request = {
        "operation": str(operation),
        "first": str(first),
        "second": str(second)
    }
    data = json.dumps(request)
    message = Message('request', 'str', data, len(data))
    return message

    
def main():
    print(calculate('add', 1, 2))

if __name__ == "__main__":
    main()