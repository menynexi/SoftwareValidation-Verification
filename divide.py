# Preconditions: Expression must be between two numbers only
def multiplication(str):
    print("number was multiplied")
    expression = str.split(" ")
    print(expression)
    print(expression.count('0'))
    if expression.count('0') == 2 and expression[-1] == '0':
        print("error was trown tried to divide by 0")
        return "ERROR"
    elif expression.count('0') == 1:
        return 0
    
    if len(expression) == 4 and expression[0] == '-':
        temp = expression[0] + expression[1]
        num1 = float(temp)
        num2 = float(expression[-1])

    elif len(expression) == 5 and expression[0] == '-' and expression[3] == '-':
        temp = expression[0] + expression[1]
        num1 = float(temp)
        num2 = float(expression[-2] + expression[-1])

    elif(expression[2] == '-'):
        temp = expression[-2] + expression[-1]
        num1 = float(temp)
        num2 = float(expression[0])
    else:
        num1 = float(expression[0])
        num2 = float(expression[-1])

    return num1 / num2

def testcases():
    assert multiplication("0 / 0") == "ERROR"
    assert multiplication("1 / 2") == 0.5
    assert multiplication("2 / - 2") == -1.0
    assert multiplication("0 / - 2") == 0.0
    assert multiplication("- 2 * - 2") == 1.0
    print("all test cases passed")

testcases()