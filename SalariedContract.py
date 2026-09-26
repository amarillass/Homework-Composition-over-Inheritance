from Composition.Contract import Contract
from Employee import Employee

class SalariedContract(Contract):
    """Contract type for an employee that's paid based on a fixed salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage 