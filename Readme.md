# ls_client

This is an example client that will encapsulate the LoanStreet API.  It's part of MVP 1 in response to the take home code quiz.

# Quick Example
- run main.py 
  - creates random loans, then updates
  - prints out all loans on the server

Current example points to aws running instance of server (http://ec2-35-175-133-100.compute-1.amazonaws.com:8888/api/all)

# Functions
    update_loan(id, Map<String, Double>) options) - updates loan with given options
    get_loan_info(id) - returns string info of loan with given id
    add_loan(amount, rate, length, payment) - creates loan with parameters, returns id

# Example usage
    street = LoanStreet(url=http://ec2-35-175-133-100.compute-1.amazonaws.com:8888/api)
    print(street.get_all_loans())

# Notes 
    client will check the server status before each call, to at least "partially" ensure server is up

