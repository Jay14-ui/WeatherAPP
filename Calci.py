def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Can't divide by zero!" if b == 0 else a / b

def main():
    print("🧮 Simple Calculator")
    print("Choose operation: +  -  *  /")
    
    op = input("Enter operator: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result:", add(a, b))
    elif op == '-':
        print("Result:", subtract(a, b))
    elif op == '*':
        print("Result:", multiply(a, b))
    elif op == '/':
        print("Result:", divide(a, b))
    else:
        print("Invalid operator.")

if __name__ == "__main__":
    main()
