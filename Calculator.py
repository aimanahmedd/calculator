a = float(input("Please enter a number: "))
b = float(input("Please enter a SECOND number: "))
operations = input("Please select an operation (+, -, *, /, ^)")
print(a, operations, b)

def calculations(a: float, b: float, operations: str) -> float:
    if operations == "+":
        result = a + b
        return result
    elif operations == "-":
        result = a - b
        return result
    elif operations == "*":
        result = a * b
        return result
    elif operations == "/":
        result = a/b
        return result
    elif operations == "^":
        result = a**b
        return result
    else:
        return 0.0
    
    
print( "=", calculations(a, b, operations))