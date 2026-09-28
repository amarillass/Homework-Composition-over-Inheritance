from Inheritance.Employee import Employee

class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.pay_rate * self.hours_worked + self.employer_cost