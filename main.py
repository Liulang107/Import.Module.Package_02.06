from application.salary import calculate_salary
from application.db.people import get_employees

def main():
  while True:
    user_input = input('Введите номер работника (1,2,3) или q для выхода: ')
    if user_input == 'q':
      print('До свидания')
      break
    calculate_salary(get_employees(user_input))

if __name__ == '__main__':
    main()