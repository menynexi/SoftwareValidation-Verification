# Preconditions: Expression must be between two numbers only
def multiplication(num1,num2):
    return num1 * num2

def testcases():
    assert multiplication(2,2) == 4.0
    assert multiplication(-2,2) == -4.0
    assert multiplication(2,-2) == -4.0
    assert multiplication(0,-2) == 0.0
    assert multiplication(2,2) == 4.0
    print("all test cases passed")

testcases()