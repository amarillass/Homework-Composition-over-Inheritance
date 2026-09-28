from Inheritance import HourlyEmployeeWithCommission


def main() -> None:
    """Main function."""
    from Employee import Employee
    from SalariedEmployee import SalariedEmployee
    from Freelancer import Freelancer
    from SalariedEmployeeWithCommission import SalariedEmployeeWithCommission

    
    henry = HourlyEmployeeWithCommission(name="Henry", id=123456, pay_rate=50, hours_worked=100)
    print(f"{henry.name} worked for {henry.hours_worked} hours and earned: ${henry.compute_pay()}.")
    
    sarah = HourlyEmployeeWithCommission(name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10)
    print(f"{sarah.name} landed {sarah.contracts_landed} contracts and earned: ${sarah.compute_pay()}.")
