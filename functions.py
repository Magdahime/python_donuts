import random


def give_filling():
    """Function to generate random choice of filling in a donut"""
    fillings = [
        'cherry', 'plum', 'oreo', 'nutella',
        'caramel-nut', 'vanilla pudding',
        'chocolate', 'fit', ]
    return random.choice(fillings)


def give_int(lower_bound, upper_bound):
    """Function to generate random calories and weight of a donut"""
    return random.randrange(lower_bound, upper_bound)


def get_filling():
    donut_filling = input("Give a filling to your donut: ")
    while not donut_filling.isalpha():
        print(f"Something went wrong! ")
        print(f"{donut_filling.title()} is not a valid donut filling")
        donut_filling = input("Try once again: ")
    return donut_filling


def get_int(lower, upper, message):
    
    number = input(message)
    while not str(number).isdigit() or int(number) < lower or int(number) > upper:
        print("\nSomething went wrong!")
        print("Remember: it cannot contain any letters")
        print(f"And it has to be a number between {lower} and {upper}")
        number = input("Try once again: ")
    return number

