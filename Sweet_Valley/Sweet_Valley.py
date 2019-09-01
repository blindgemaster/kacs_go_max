from datetime import date
import os

clear = lambda: os.system('cls')
print('                 Sweet Valley')
print('')
print('')


class BakeryEmployee:
    def __init__(self, name, pay):
        self.dishes = 0
        self.pay = pay
        self.sell_list = []
        self.total = 0
        self.name = name

    def dish_done(self):
        price = int(input('Product Price: '))
        self.sell_list.append(price)
        self.dishes += 1

    def get_dishes(self):
        return self.dishes

    def employee_total(self):
        if self.total == 0:
            for items in self.sell_list:
                self.total += items
            return self.total
        else:
            return self.total

    def get_name(self):
        return self.name


emp_1 = BakeryEmployee('Nasir', 2500)
emp_2 = BakeryEmployee('Ali', 3500)
emp_3 = BakeryEmployee('Khan', 1500)
print("Enter '000' to end the Program")

while True:
    try:
        flag = False
        clear()
        print('                                               Sweet Valley')
        print('')
        print('')
        print("Enter '000' to end the Program")
        id_of_employee = int(input('Enter ID: '))
        if id_of_employee == 000:
            clear()
            pay_total = emp_1.pay + emp_2.pay + emp_3.pay
            complete_total = emp_1.employee_total() + emp_2.employee_total() + emp_3.employee_total()
            my_total = complete_total - pay_total
            print(f'Name|Deals|Total|Pay\n'
                  f'{emp_1.get_name()} | {emp_1.get_dishes()} | {emp_1.employee_total()} | {emp_1.pay}\n'
                  f'{emp_2.get_name()} | {emp_2.get_dishes()} | {emp_2.employee_total()} | {emp_2.pay}\n'
                  f'{emp_3.get_name()} | {emp_3.get_dishes()} | {emp_3.employee_total()} | {emp_3.pay}\n'
                  f'Total Earning = {complete_total}\n'
                  f'Total Pays = {pay_total}\n'
                  f'Profit = {my_total}\n')
            with open('logs.txt', 'a') as f:
                today = date.today()
                f.write(f'{today}  | Profit =  {my_total} | Sales = {complete_total}\n')
            break
        elif id_of_employee == 1:
            emp_1.dish_done()
            flag = True
        elif id_of_employee == 2:
            emp_2.dish_done()
            flag = True
        elif id_of_employee == 3:
            flag = True
            emp_3.dish_done()
        if not flag:
            print('Your values are incorrect')
    except ValueError:
        print('Please input a valid choice')
input()
