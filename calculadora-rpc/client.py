import rpyc

try:
    connection = rpyc.connect('localhost', 3000)
    calculator = connection.root
    print(calculator.add(1, 2))
    print(calculator.sub(2, 1))
    print(calculator.div(500, 2))
    print(calculator.mul(21, 10))
except:
    print("Um erro ocorreu")