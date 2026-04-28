# the pizza machineeeeeeeeeeeeeeeeeeeeeeeeeeeee

class pizza:
    def __init__(self, base, ingredients, price):
        self.base = base
        self.ingredients = ingredients
        self.price = price

calzone = pizza(base=['tomato'], ingredients=['chicken', 'cheese', 'tomato'], price=('20$'))
margherita = pizza(base=['tomato'], ingredients=['tomato', 'cheese', 'basil'], price=('12$'))

print("Welcome to our wonderful restaurant, we are delighted to have you")
print("We offer you two pizzas: calzone and margherita")

choice = input("Which pizza would you like? ")

if choice == 'calzone':

    print("You chose the calzone")

    base = input("Which base would you like? (tomato, cream) ")

    calzone.base.remove('tomato')
    calzone.base.append(base)

    print(f"Your pizza base is {calzone.base}")

    ingredients = input(f"Which ingredient would you like to add? (current ingredients: {calzone.ingredients})")

    calzone.ingredients.append(ingredients)

    yes = input("Would you like to add another ingredient? (yes/no) ")

    if yes == "yes":
        ingredients = input(f"Which ingredient would you like to add? (current ingredients: {calzone.ingredients})")
        calzone.ingredients.append(ingredients)
        print(f"Your pizza ingredients are {calzone.ingredients}")

    elif yes == "no":
        print("Okay, let's continue")

    else:
        print("Please answer yes or no only, try again")
        exit()

    print(f"Your pizza ingredients are {calzone.ingredients}")
    print(f"Your pizza will be made with {calzone.base} {calzone.ingredients}")

    payment = input(f"The total price is {calzone.price}. Would you like to pay? (yes/no) ")
    
    if payment == "yes":
        print("Thank you for your purchase")

    elif payment == "no":
        print("Goodbye")
        exit()

    else:
        print("Please answer yes or no only, try again")
        exit()

    table = input("Which table would you like to eat at? ")
    
    print(f"Your pizza will be ready in 15 minutes at table n°{table}")

elif choice == 'margherita':

    print("You chose the margherita")

    base = input("Which base would you like? (tomato, cream) ")

    margherita.base.remove('tomato')
    margherita.base.append(base)

    print(f"Your pizza base is {margherita.base}")

    ingredients = input(f"Which ingredient would you like to add? (current ingredients: {margherita.ingredients})")

    margherita.ingredients.append(ingredients)

    yes = input("Would you like to add another ingredient? (yes/no) ")

    if yes == "yes":
        ingredients = input(f"Which ingredient would you like to add? (current ingredients: {margherita.ingredients})")
        margherita.ingredients.append(ingredients)
        print(f"Your pizza ingredients are {margherita.ingredients}")

    elif yes == "no":
        print("Okay, let's continue")
      
    else:
        print("Please answer yes or no only, try again")
        exit()

    print(f"Your pizza ingredients are {margherita.ingredients}")
    print(f"Your pizza will be made with {margherita.base} {margherita.ingredients}")

    payment = input(f"The total price is {margherita.price}. Would you like to pay? (yes/no) ")
    
    if payment == "yes":
        print("Thank you for your purchase")

    elif payment == "no":
        print("Goodbye")
        exit()

    else:
        print("Please answer yes or no only, try again")
        exit()

    table = input("Which table would you like to eat at? ")
    
    print(f"Your pizza will be ready in 15 minutes at table n°{table}")

else:
    print("This pizza is not available in this restaurant")
