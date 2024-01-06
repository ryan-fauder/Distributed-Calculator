class Calculator:
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        if (b == 0):
            print("Não é possível realizar divisão por 0")
            return None
        return a / b