# Preconditions: Expression must be between two numbers only
def addition(str):
    print("number was added")
    expression = str.split(" ")
    if len(expression) >= 4 and expression[0] == '-':
        temp = expression[0] + expression[1]
        num1 = float(temp)
        num2 = float(expression[-1])
    elif(expression[2] == '-'):
        temp = expression[-2] + expression[-1]
        num1 = float(temp)
        num2 = float(expression[0])
    else:
        num1 = float(expression[0])
        num2 = float(expression[-1])
    return num1 + num2

def testcases():
    assert addition("2 + 2") == 4.0
    assert addition("- 2 + 2") == 0.0
    assert addition("2 + - 2") == 0.0
    assert addition("0 + - 2") == -2.0
    print("all test cases passed")

testcases()