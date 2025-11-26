class Calculator:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        return a * b
    
    @staticmethod
    def calculate_total(*x: float, costs: list[float] | None = None) -> float:
        """
        Calculate the sum of given numbers.

        Accepts either a variable list of positional float arguments or a single
        keyword argument `costs` which is an iterable (list/tuple) of floats.

        Examples:
            calculate_total(1, 2, 3)
            calculate_total(costs=[1, 2, 3])

        Returns 0.0 when nothing is provided.

        Args:
            *x (float): Zero or more positional float arguments.
            costs (list[float] | None): Optional iterable of costs.

        Returns:
            float: Sum of the provided numbers.
        """
        if costs is not None:
            # Accept both lists/tuples and single numeric values
            if isinstance(costs, (list, tuple)):
                return sum(costs)
            try:
                return float(costs)
            except Exception:
                # If costs is not iterable and not convertible to float fall back to 0
                return 0.0

        # No costs keyword provided — sum any positional args
        if x:
            return sum(x)

        return 0.0
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Calculate daily budget

        Args:
            total (float): Total cost.
            days (int): Total number of days

        Returns:
            float: Expense for a single day
        """
        return total / days if days > 0 else 0
    
    
