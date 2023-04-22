# Preconditions: Expression must be between two numbers only
def multiplication(str):
    print("number was multiplied")
    expression = str.split(" ")
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
    return num1 * num2

def testcases():
    assert multiplication("2 * 2") == 4.0
    assert multiplication("- 2 * 2") == -4.0
    assert multiplication("2 * - 2") == -4.0
    assert multiplication("0 * - 2") == 0.0
    assert multiplication("- 2 * - 2") == 4.0
    print("all test cases passed")

testcases()