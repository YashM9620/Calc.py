from calc import SimpleCalculator

class Test_SimpleCalculatorMultiplication:

    def test_multiplication_case1(self):
        result = SimpleCalculator.multiply(5,2)
        assert result == 10

    def test_multiplication_case2(self):
        result = SimpleCalculator.multiply(20,6)
        assert result == 120

    def test_multiplication_case3(self):
        result = SimpleCalculator.multiply(9,8)
        assert result == 72
