def square(num1, num2):
    return num1 ** num2

    
def testcases():
    assert square(2,2) == 4.0
    assert square(3,2) == 9.0
    assert square(-2,2) == 4
    assert square(0,2) == 0.0
    assert square(2.5,2) == 6.25
    print("all test cases passed")
    
testcases()