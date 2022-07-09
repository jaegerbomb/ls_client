from LoanStreet import LoanStreet
from constants import api_url, api_url_aws

if __name__ == "__main__":
    street = LoanStreet(url=api_url_aws)
    print(street.check_health())
    loan_id = f'{street.add_loan(500000, 3.32323, 30, 40)}'
    # add a few more loans
    print(f'{street.add_loan(500000, 1.23093, 10, 10)}')
    print(f'{street.add_loan(600000, 2.09230, 20, 110)}')
    print(f'{street.add_loan(700000, 3.0239230, 30, 2353)}')
    print(f'{street.add_loan(800000, 4.2023930, 330, 20)}')

    print(f'Loan info = {street.get_loan_info(loan_id)}\n')
    new_loan_options = {"id": loan_id, "amount": 5000}
    print(street.update_loan(new_loan_options))
    print(f'Loan info = {street.get_loan_info(loan_id)}')
    new_loan_options = {"id": loan_id, "rate": 2.52309}
    print(street.update_loan(new_loan_options))
    print(f'Loan info = {street.get_loan_info(loan_id)}')
    new_loan_options = {"id": loan_id, "length": 25}
    print(street.update_loan(new_loan_options))
    print(f'Loan info = {street.get_loan_info(loan_id)}')
    new_loan_options = {"id": loan_id, "payment": 100}
    print(street.update_loan(new_loan_options))
    print(f'Loan info = {street.get_loan_info(loan_id)}')

    # let's update all of them
    new_loan_options["amount"] = 25000
    new_loan_options["rate"] = 1.9999
    new_loan_options["length"] = 24
    new_loan_options["payment"] = 275
    print(street.update_loan(new_loan_options))
    print(f'Loan info = {street.get_loan_info(loan_id)}')

    # now print all loans
    print(street.get_all_loans())









