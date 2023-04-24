# Preconditions: Expression must be between two numbers only
def addition(num1,num2):
    return num1 + num2


def testcases():
    assert addition(2,2) == 4.0
    assert addition(-2,2) == 0.0
    assert addition(2,-2) == 0.0
    assert addition(0,-2) == -2.0
    print("all test cases passed")

testcases()