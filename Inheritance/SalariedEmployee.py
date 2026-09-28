from Employee import Employee

class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.monthly_salary * self.percentage 