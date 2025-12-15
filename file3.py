# 始终生效

def main():
    print("Hello from file3")

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def greet(name):
    return f"Hello, {name}!"

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def get_history(self):
        return self.history
