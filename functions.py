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

