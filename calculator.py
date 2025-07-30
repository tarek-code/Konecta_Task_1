def add(a,b):
    #Returns the sum of a and b.
    return a + b
def subtract(a, b):
    #Returns the difference of a and b.
    return a + b # bug intentional
def multiply(a, b):
    #Returns the product of a and b.
    return a * b
def divide(a, b):
    #Returns the quotient of a and b.
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
print("This is a simple calculator module.")

if __name__ == "__main__":
    print("Testing the calculator functions...")
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 from 10:", subtract(10, 5))
    print("Multiplication of 4 and 6:", multiply(4, 6))
    print("Division of 8 by 2:", divide(8, 2))