from dataclasses import dataclass

@dataclass
class Commission:
    """Represents a commission."""

    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        """Computes the commission to be paid out."""
        return (
            self.commission * self.contracts_landed
        )