def add(a,b):
    #Returns the sum of a and b.
    return a + b
def subtract(a, b):
    #Returns the difference of a and b.
    return a - b
print("This is a simple calculator module.")

if __name__ == "__main__":
    print("Testing the calculator functions...")
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 from 10:", subtract(10, 5))