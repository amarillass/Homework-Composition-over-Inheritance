from Composition import Contract, Commission, Employee
from Composition import HourlyContract, FreelancerContract, SalariedContract


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=123456, contract=henry_contract)
    print(f"{henry.name} worked for {henry_contract.hours_worked} hours and earned: ${henry.compute_pay()}.")
    
    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = Commission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission)
    print(f"{sarah.name} worked landed {sarah_commission.contracts_landed} contracts and earned: ${sarah.compute_pay()}.")
    