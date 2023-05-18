# import TODO as TODO

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
    "money": 0,
}


def report():
    water_data = resources["water"]
    milk_data = resources["milk"]
    coffee_data = resources["coffee"]
    money_data = resources["money"]
    print(f" Water: {water_data}ml\n"
          f" Milk: {milk_data}ml\n"
          f" Coffee: {coffee_data}g\n"
          f" Money: ${money_data}")


# TODO: 3. Process Coins
# TODO: 4. Check how many money was payed

def cost():
    def quarters_coins():
        quarters = int(input("how many quarters?: "))
        coins = quarters * 0.25
        return coins

    def dimes_coins():
        dimes = int(input("how many dimes?: "))
        coins = dimes * 0.1
        return coins

    def nickles_coins():
        nickles = int(input("how many nickles?: "))
        coins = nickles * 0.05
        return coins

    def pennies_coins():
        pennies = int(input("how many pennies?: "))
        coins = pennies * 0.01
        return coins

    quarters_c = quarters_coins()
    dimes_c = dimes_coins()
    nickles_c = nickles_coins()
    pennies_c = pennies_coins()
    total = quarters_c + dimes_c + nickles_c + pennies_c

    return total


# TODO: 2. Check if the resources are sufficient for caffe we want


def enough_resources():
    for key in ingredients_dict:
        value = ingredients_dict[key]
        for key_resources in resources:
            value_resources = resources[key_resources]
            if key == key_resources:
                if value <= value_resources:
                    return True
                else:
                    print(f"Not enough {key_resources}")
                    return False

# TODO: 8. Resourcer will be updated


def update_resources():
    for key in ingredients_dict:
        resources[key] -= ingredients_dict[key]
    print(resources)


make_coffee_possible = True

while make_coffee_possible:
    choice = input("What would you like:? (espresso/ latte/ cappuccino): ").lower()

    # TODO: 1. Print report, the resources values will be printed

    if choice == "report":
        report()
    # TODO: 9. Turn off the Coffee Machine by entering OFF the prompt.
    elif choice == "off":
        make_coffee_possible = False

    else:
        my_choice = MENU[choice]
        ingredients_dict = my_choice["ingredients"]

        if not enough_resources():
            make_coffee_possible = False


# TODO: 5. Check if are sufficient money payed
        else:
            print("Please insert coins. ")
            money_payed = cost()
            money_need = my_choice["cost"]

# TODO: 7. If are sufficient money and resources Make a Caffe
            if money_payed == money_need:
                print(f"Here is your {choice} ☕️. Enjoy!")
                resources["money"] += money_need
                update_resources()
            elif money_payed < money_need:
                print("Sorry that's not enough money. Money refunded.")

# TODO: 6. If the user has inserted too much money, the machine should offer change.

            elif money_payed > money_need:
                print(f"Here is your {choice} ☕️. Enjoy!")
                rest = money_payed - money_need
                rest1 = round(rest, 2)
                print(f"Here is ${rest1} in change.")
                resources["money"] += money_need
                update_resources()












