import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           
        (0, 0, 0),           
        (-1, 1, 0),          
        (2.5, 3.5, 6.0),     
        (-2.5, 3.5, 1.0),    
    ],

ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float",
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
     result = Operations.addition(a, b)
     assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"


























































#import pytest
#from app.operations import addition, subtraction, multiplication, division

#def test_addition ():
     #assert addition(1, 3) == 4
   

#def test_subtraction():
   # assert subtraction(1, 1) == 0


#def test_multiplication():
    #assert multiplication(2,3) == 6

#def test_division():
    #assert division(8,2) == 4

    #def test_division_positive():
       # assert division(6, 2) == 3

    #def test_division_negative():
       # with pytest.raises(ValueError, match="Division by zero is not allowed"):
            #division(1, 0)  
