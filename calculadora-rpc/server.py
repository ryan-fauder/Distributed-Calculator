import rpyc
from rpyc.utils.server import ThreadedServer

@rpyc.service
class Calculator(rpyc.Service):
    @rpyc.exposed
    def add(self, a, b):
        return a + b
    @rpyc.exposed
    def sub(self, a, b):
        return a - b
    @rpyc.exposed
    def mul(self, a, b):
        return a * b
    @rpyc.exposed
    def div(self, a, b):
        if (b == 0):
            print("Não é possível realizar divisão por 0")
            return None
        return a / b
if __name__ == "__main__":
    server = ThreadedServer(Calculator, port = 3000)
    print("Servidor iniciado")
    server.start()