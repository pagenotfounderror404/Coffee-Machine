import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report():
    return resources
def off():
    sys.exit()
def check():
    global c
    if c=="espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("There is not enough water to make espresso. ")
            sys.exit()
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("There is not enough coffee to make espresso. ")
            sys.exit()
    elif c=="latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("There is not enough water to make latte. ")
            sys.exit()
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("There is not enough coffee to make latte. ")
            sys.exit()
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("There is not enough milk to make latte. ")
            sys.exit()
    elif c=="capuccino":
        if resources["water"]< MENU["capuccino"]["ingredients"]["water"]:
            print("There is not enough water to make capuccino. ")
            sys.exit()
        elif resources["coffee"]< MENU["capuccino"]["ingredients"]["coffee"]:
            print("There is not enough coffee to make capuccino. ")
            sys.exit()
        elif resources["milk"]< MENU["capuccino"]["ingredients"]["milk"]:
            print("There is not enough milk to make capuccino. ")
            sys.exit()
def money():
    global c
    q=int(input("Enter the number of quarters: "))
    d=int(input("Enter the number of dimes: "))
    n=int(input("Enter the number of nickels: "))
    p=int(input("Enter the number of pennies: "))
    t=0.25*q+0.10*d+0.05*n+0.01*p
    if c== 'espresso':
        if t<MENU["espresso"]["cost"]:
            print(f"Your order couldn't be processed. You have provided insufficient money as per your requirement. You refund of {t} has been initiated. ")
        else:
            if t==MENU["espresso"]["cost"]:
                print("Your order is ready.")
            elif t > MENU["espresso"]["cost"]:
                k=round(t-MENU["espresso"]["cost"],2)
                print(f"Your order is ready. Here is your change ${k} ")
            resources["water"]= resources["water"]-MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    if c=='cappuccino':
        if t < MENU["cappuccino"]["cost"]:
            print(f"Your order couldn't be processed. You have provided insufficient money as per your requirement. You refund of {t} has been initiated. ")
        else:
            if t==MENU["cappuccino"]["cost"]:
                print("Your order is ready.")
            elif t > MENU["cappuccino"]["cost"]:
                k=round(t-MENU["cappuccino"]["cost"],2)
                print(f"Your order is ready. Here is your change ${k} ")
            resources["water"]= resources["water"]-MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
    if c=='latte':
        if t < MENU["latte"]["cost"]:
            print(f"Your order couldn't be processed. You have provided insufficient money as per your requirement. You refund of {t} has been initiated. ")
        else:
            if t==MENU["latte"]["cost"]:
                print("Your order is ready.")
            elif t > MENU["latte"]["cost"]:
                k=round(t-MENU["latte"]["cost"],2)
                print(f"Your order is ready. Here is your change ${k} ")
            resources["water"]= resources["water"]-MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]

while True:
    c= input("What do you want to order? Type Espresso, Latte or Cappuccino: ").lower()
    if c=='off':
        off()
    elif c=='report':
        print(report())
    else:
        if c == 'espresso' or c == 'latte' or c == 'cappuccino':
            check()
            money()
        else:
            print("This item doesn't exist in our menu")
            continue



