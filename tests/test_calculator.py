import pytest
from io import StringIO
from app.calculator import display_help, display_history, calculator


def test_display_help(capsys):
    display_help()
    captured = capsys.readouterr()
    expected_output = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
"""
    assert captured.out.strip() == expected_output.strip()

def test_display_history_empty(capsys):
    history = []
    display_history(history)
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."


def test_display_history_with_entries(capsys):
    history = [
        "AddCalculation: 10.0 Add 5.0 = 15.0",
        "SubtractCalculation: 20.0 Subtract 3.0 = 17.0",
        "MultiplyCalculation: 7.0 Multiply 8.0 = 56.0",
        "DivideCalculation: 20.0 Divide 4.0 = 5.0"
    ]
    display_history(history)
    captured = capsys.readouterr()
    expected_output = """Calculation History:
1. AddCalculation: 10.0 Add 5.0 = 15.0
2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0
3. MultiplyCalculation: 7.0 Multiply 8.0 = 56.0
4. DivideCalculation: 20.0 Divide 4.0 = 5.0"""
    assert captured.out.strip() == expected_output.strip()
