def square(number_string):
    expression = number_string.split(" ")
    if len(expression) == 3 and expression[1] == '**' and float(expression[2]) == 2:
        num = float(expression[0])
        if num < 0:
            result = -1 * (abs(num) ** 2)
        else:
            result = num ** 2
        return result
    else:
        return None

    
def testcases():
    assert square("2 ** 2") == 4.0
    assert square("3 ** 2") == 9.0
    assert square("-2 ** 2") == -4
    assert square("0 ** 2") == 0.0
    assert square("2.5 ** 2") == 6.25
    print("all test cases passed")
    
testcases()