# Preconditions: Expression must be between two numbers only
def subtraction(num1, num2):
    return num1 - num2

def testcases():
    assert subtraction(2,-2) == 4
    assert subtraction(-2,2) == -4
    assert subtraction(0,2) == -2.0
    assert subtraction(-2,-2) == 0.0
    print("all test cases passed")

testcases()