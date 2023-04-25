# Preconditions: Expression must be between two numbers only
def subtraction(num1, num2):
    return num1 - num2

def testcases():
    # Test two positive integers
    assert subtraction(5, 3) == 2
    
    # Test two negative integers
    assert subtraction(-5, -3) == -2
    
    # Test a positive and a negative integer
    assert subtraction(5, -3) == 8
    
    # Test two positive floats
    assert subtraction(3.5, 1.2) == 2.3
    
    # Test two negative floats
    assert subtraction(-3.5, -1.2) == -2.3
    
    # Test a positive and a negative float
    assert subtraction(3.5, -1.2) == 4.7
    
    # Test a positive integer and a negative float
    assert subtraction(5, -1.2) == 6.2
    
    # Test a negative integer and a positive float
    assert subtraction(-5, 1.2) == -6.2

    # Test a positive or negative integer or float and zero
    assert subtraction(5, 0) == 5
    assert subtraction(-5, 0) == -5
    assert subtraction(5.0, 0.0) == 5.0
    assert subtraction(-5.0, 0.0) == -5.0
    print("all test cases passed")

testcases()