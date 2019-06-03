def calculate_salary(employee):
    salary = int(employee.days) * int(employee.rate)
    print(f'Заработная плата: {salary}')