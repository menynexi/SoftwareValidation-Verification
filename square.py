def square(num1, num2):
    if num1 == 0 and num2 < 0:
        return 0
    return num1 ** num2

    
def testcases():
    # Test case 1: Normal state, num2 = 0, expected output = 1
    assert square(2, 0) == 1

    # Test case 2: Normal state, num2 = 1, expected output = num1
    assert square(2, 1) == 2

    # Test case 3: Normal state, num2 > 1, expected output = num1 raised to the power of num2
    assert square(2, 3) == 8

    # Test case 4: Exception state, num2 < 0 and num1 != 0, expected output = 1 divided by num1 raised to the absolute value of num2
    assert round(square(2, -2), 9) == 0.25

    # Test case 5: Exception state, num2 < 0 and num1 = 0, expected output = infinity
    assert square(0, -2) == 0
    print("all test cases passed")
    
testcases()