from collections import namedtuple

import sys

import time

item = namedtuple("item", 'name price')

items = (item('Tea', 20), item('Cofee', 30), item('Shawarma', 100), item('Biryani', 120), item('Milkshake Banana', 60))


def display():
    for item in items:
        print(item.name)
        print('\033[1;1H' + str(item.price))


print("*************** Welcome to Islamabad Cafề ***************")
while True:
    print("\n1. Place Order\n2. Track Order\n3. Exit")
    option = int(input("Select Option: "))
    if option == 1:
        display()
    elif option == 2:
        print()
    elif option == 3:
        print("\n\nThank you for visiting Islamabad Cafề\n")
        exit()
    else:
        print("INVALID OPTION!!")
