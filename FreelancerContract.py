from Composition import Contract
from Inheritance.Employee import Employee

class FreelancerContract(Contract):
    """Contract type for a freelancer that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return (
            self.pay_rate * self.hours_worked
        )