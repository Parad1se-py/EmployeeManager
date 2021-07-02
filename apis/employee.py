import sqlite3
from sqlite3 import *

conn = sqlite3.connect('employee.db')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#    first text,
#    last text,
#    salary integer
#    )
#""")

class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self) -> str:
        return f"Employee('{self.first}' '{self.last}' '{self.pay}')"

    def commit(self):
        conn.commit()

    def add_emp(self, first:str, last:str, sal:int) -> None:
        """This is used for adding any new employees into the db"""
        print("Inserting values...")
        c.execute("INSERT INTO employees VALUES (?, ?, ?)",(first, last, sal))
        conn.commit()
        print(f"Added information\nFirst : {first}\nLast : {last}\nSalary : {sal}")

    def close(self):
        conn.close()
