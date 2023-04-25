# Preconditions: Expression must be between two numbers only
def divide(num1, num2):
    return num1 / num2

    

def testcases():
    assert divide(1,2) == 0.5
    assert divide(2,-2) == -1.0
    assert divide(0,-2) == 0.0
    assert divide(-2,-2) == 1.0

    assert divide(10,2) == 5.0
    assert divide(-10,-2) == 5.0
    assert divide(10,-2) == -5.0
    assert divide(10.5,2.5) == 4.2
    assert divide(-10.5,-2.5) ==4.2
    assert divide(10.5,-2.5) ==-4.2
    assert divide(10,-2.5) == -4     
    assert divide(-10,2.5) == -4.0
    print("all test cases passed")

testcases()