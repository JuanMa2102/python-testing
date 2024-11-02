import unittest
from src.calculator import sum, subtract, multiply, divide

class CalculatorTest( unittest.TestCase ):  
    def test_sum( self ):
         assert sum( 1, 2 ) == 3
        
    def test_substract(self):
        assert subtract( 10,5 ) == 5
        
    def test_multiply(self):
        assert multiply(3, 2) == 6

    def test_divide(self):
        result = divide(10, 2)
        expected = 5
        assert result == expected
    
    def test_divide_by_0( self ):
         with self.assertRaises(ZeroDivisionError):
            divide(3, 0)