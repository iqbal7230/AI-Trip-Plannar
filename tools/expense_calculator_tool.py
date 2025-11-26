from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night:float, total_days:float) -> float:
            """Calculate total hotel cost"""
            return self.calculator.multiply(float(price_per_night), float(total_days))
        
        @tool
        def calculate_total_expense(*args: float, costs: list[float] | None = None) -> float:
            """Calculate total expense of the trip.

            Accepts either positional numbers, or a keyword `costs` containing an
            iterable (list/tuple) of numbers. This keeps the tool backwards
            compatible with positional usage while allowing callers (or the
            agent framework) to pass a `costs=` keyword.
            """
            if costs is not None:
                if isinstance(costs, (list, tuple)):
                    return self.calculator.calculate_total(*costs)
                try:
                    return self.calculator.calculate_total(float(costs))
                except Exception:
                    return 0.0

            # fallback to positional args
            return self.calculator.calculate_total(*args)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]