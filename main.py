import apis.employee
from apis.employee import *

option = input("Enter \"add\" in the terminal to add a new emplyee into the db.\nEnter \"close\" in the terminal to close.\nYour option : ")

if option == 'add':
    self = None
    first = input('Input first name of employee : ')
    last = input('Input last name of employee : ')
    salary = input('Input the salary of employee : ')
    Employee.add_emp(self, first, last, int(salary))
    option = input("Enter \"add\" in the terminal to add a new emplyee into the db.")

if option == 'close':
    self = None
    print('Closing...')
    Employee.close(self)
    print('Closed')

else:
    print("That's not a valid option!")
    option = input("Enter \"add\" in the terminal to add a new emplyee into the db.")
