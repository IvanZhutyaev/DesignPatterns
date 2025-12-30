from abc import ABC, abstractmethod
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value
    
    def interpret(self):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self):
        return self.left.interpret() * self.right.interpret()

# Парсер (упрощенный)
def parse_expression(tokens):
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(Number(int(token)))
        elif token == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(Add(left, right))
        elif token == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(Subtract(left, right))
        elif token == '*':
            right = stack.pop()
            left = stack.pop()
            stack.append(Multiply(left, right))
    
    return stack.pop()

# Использование
# Польская нотация: "2 3 + 4 *" = (2+3)*4 = 20
expression = parse_expression(["2", "3", "+", "4", "*"])
result = expression.interpret()
print(f"Выражение: 2 3 + 4 *")
print(f"Результат: {result}")

# Еще пример: "5 2 * 3 +" = (5*2)+3 = 13
expression2 = parse_expression(["5", "2", "*", "3", "+"])
result2 = expression2.interpret()
print(f"\nВыражение: 5 2 * 3 +")
print(f"Результат: {result2}")