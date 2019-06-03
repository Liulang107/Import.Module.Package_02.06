from application.salary import *
from application.db.people import *

def dirty_main():
  while True:
    user_input = input('Введите номер работника (1,2,3) или q для выхода: ')
    if user_input == 'q':
      print('До свидания')
      break
    calculate_salary(get_employees(user_input))

if __name__ == '__main__':
    dirty_main()