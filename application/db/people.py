from application.db.dict import employees

class Employee:
    def __init__(self, name, days=None, rate=None):
        self.name = name
        self.days = days
        self.rate = rate


def get_employees(number):
    for person in employees:
        if number == person['number']:
            employee = Employee(person['name'], person['days'], person['rate'])
            print('Имя работника: ', person['name'])
    return employee
