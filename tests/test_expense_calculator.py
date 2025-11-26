import pytest

from utils.expense_calculator import Calculator


def test_calculate_total_positional():
    assert Calculator.calculate_total(1, 2, 3) == 6


def test_calculate_total_costs_list():
    assert Calculator.calculate_total(costs=[1, 2, 3, 4]) == 10


def test_calculate_total_costs_single():
    assert Calculator.calculate_total(costs=5) == 5


def test_calculate_total_empty():
    assert Calculator.calculate_total() == 0.0
