from HourlyEmployee import HourlyEmployee

class HourlyEmployeeWithCommission(HourlyEmployee):
    """Employee that's paid based on number of worked hours with commission."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return super().compute_pay() + self.commission * self.contracts_landed 