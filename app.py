def sum(a, b): 
    return a + b

def sub(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

print(sum(1, 2))
print(sub(5, 2))
print(division(8, 2))