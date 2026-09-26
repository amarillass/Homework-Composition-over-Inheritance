from abc import ABC, abstractmethod
from typing import Optional
from Composition import Commission, Contract

class Employee(ABC):
    """Basic representation of an employee at the company."""
    name: str
    id: int
    contract: Contract
    commission: Optional[Commission.Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout
