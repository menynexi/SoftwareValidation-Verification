# Preconditions: Expression must be between two numbers only
def divide(num1, num2):
    try:
        return num1 / num2
    except:
        return "ERROR"

    

def testcases():
    assert divide(0,0) == "ERROR"
    assert divide(1,2) == 0.5
    assert divide(2,-2) == -1.0
    assert divide(0,-2) == 0.0
    assert divide(-2,-2) == 1.0
    print("all test cases passed")

testcases()