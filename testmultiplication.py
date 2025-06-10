
from calc import SimpleCalculator

class Test_SimpleCalculatorMultiplication:

    def test_multiplication_case1():
        calculator = SimpleCalculator() # Instantiate the calculator
        result = calculator.multiply(5, 2)
        if result == 10:
            print("test_multiplication_case1: PASSED")
        else:
            print(f"test_multiplication_case1: FAILED - Expected 10, got {result}")
        assert result == 10 

    def test_multiplication_case2():
        calculator = SimpleCalculator()
        result = calculator.multiply(20, 6)
        if result == 120:
            print("test_multiplication_case2: PASSED")
        else:
            print(f"test_multiplication_case2: FAILED - Expected 120, got {result}")
        assert result == 120

    def test_multiplication_case3():
        calculator = SimpleCalculator()
        result = calculator.multiply(9, 8)
        if result == 72:
            print("test_multiplication_case3: PASSED")
        else:
            print(f"test_multiplication_case3: FAILED - Expected 72, got {result}")
        assert result == 7

test_multiplication_case1
