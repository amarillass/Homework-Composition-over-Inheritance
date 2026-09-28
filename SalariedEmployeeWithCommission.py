from SalariedEmployee import SalariedEmployee

class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that's paid based on a fixed salary and that gets a commission."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (super().compute_pay()) + self.commission * self.contracts_landed