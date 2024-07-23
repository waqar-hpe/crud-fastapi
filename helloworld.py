
def doSum():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a+b

def doSubtraction():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return float(a)-float(b)

def doMultiplication():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return float(a) * float(b)

def doDivision():
    a = input("Enter first number(divident): ")
    b = input("Enter second number(divisor): ")
    if float(b) == 0.0:
        return "error: divisor can't be zero"
    return float(a) / float(b)
def performOperation(op):
    match op:
        case 1:
            sum = doSum()
            print(f"The result of sum is: {sum}")
        case 2:
            sub = doSubtraction()
            print(f"The result of subtraction is: {sub}")
        case 3:
            m = doMultiplication()
            print(f"The result of subtraction is: {m}")
        case 4:
            d = doDivision()
            print(f"The result of subtraction is: {d}")

operation = int(input("which Operation do you want to perform? \n"
      "1. SUM \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n"))

performOperation(operation)




