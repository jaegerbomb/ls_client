from LoanStreet import LoanStreet
from constants import api_url

if __name__ == "__main__":
    street = LoanStreet(url=api_url)
    print(street.check_health())
    loan_id = f'{street.add_loan(500000, 3.32323, 30, 40)}'
    print(f'Create loan {loan_id}')




