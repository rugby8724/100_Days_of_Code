from os import system
import time

from coffee_data import MENU, resources

# TODO 1: ask what would you like


def report_resources():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    if 'money' not in resources:
        resources['money'] = 0
    print(f'Money: ${resources["money"]}')


def check_resources(coffee):
    for k, v in coffee['ingredients'].items():
        if resources[k] < v:
            print(f'please refill the {k}')
            return False


def payment(coffee):
    price = coffee['cost']
    pay = 0
    currency = {
        'dollars': 1,
        'quarters': .25,
        'dimes': .1,
        'nickels': .05,
        'pennies': .01
    }

    for k, v in currency.items():
        print(f'Please insert ${price - pay}')
        pay += int(input(f'How many {k}? ')) * v
        if pay >= price:
            break
    if pay < price:
        print(f'Did not enter enough money returning $ {pay}')
        return False
    else:
        print('Making coffee')
        if 'money' in resources:
            resources['money'] += price
        else:
            resources['money'] = price
        print(resources['money'])
        if pay > price:
            print(f'Here is your change ${pay-price}')


def decrease_inv(coffee):
    for k, v in coffee['ingredients'].items():
        resources[k] -= v


def get_coffee():
    making_coffee = True
    resource = True
    pay = True
    choice = input('What would you like? espresso/latte/cappuccino? ').lower()
    if choice in MENU:
        coffee = MENU[choice]
    elif choice == 'report':
        report_resources()
        making_coffee = False
    elif choice == 'off':
        print('GoodBye')
        time.sleep(2)
        system('clear')
        exit()
    else:
        making_coffee = False
    while making_coffee and resource and pay:
        resource = check_resources(coffee)
        print('Enough resources')
        pay = payment(coffee)
        decrease_inv(coffee)
        print(f'Here is your {choice} enjoy!')
    get_coffee()


get_coffee()
