from Inheritance.Employee import Employee

class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
        )