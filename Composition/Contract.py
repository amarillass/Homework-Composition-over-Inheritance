from abc import ABC, abstractmethod

class Contract(ABC):
    """Represents a contract and payment process for a particular employee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Computes how much to pay an employee at the company under this contract."""
