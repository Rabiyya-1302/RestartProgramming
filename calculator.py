
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

op = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
 should_accumulate=True
 n1 = float(input("Enter First Value: "))

 while should_accumulate:
    operation = input("Operation (+,-,*,/): ")
    n2 = float(input("Enter Second Value: "))

    result = op[operation](n1, n2)

    print("Result =", result)

    choice = input( "Continue with previous result? (Y/N): " )

    if choice.upper() == "Y":
        n1 = result      # use previous result
    else:
       should_accumulate=False
       calculator()
     
calculator()
    
