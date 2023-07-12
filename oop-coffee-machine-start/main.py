from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
e=Menu()
Co=CoffeeMaker()
m=MoneyMachine()
score=True
while score:
    print("We have " + e.get_items() + " in our menu")
    c = input("What is your order. Enter latte/espresso/cappuccino").lower()
    if c=='profit':
        m.report()
    elif c == 'report':
        Co.report()
    elif c =='exit':
        score=False
    else:
        k = e.find_drink(c)
        score=m.make_payment(k.cost)
        if score:
            if Co.is_resource_sufficient(k):
                Co.make_coffee(k)


