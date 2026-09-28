from Composition import Contract
from Inheritance.Employee import Employee

class HourlyContract(Contract):
    """Contract type for an employee that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost