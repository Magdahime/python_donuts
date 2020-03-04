import functions as f
from donut import Donut
from stomach import Stomach
import operator


def greedy_algorithm(donuts, stomach):
    eaten_calories = 0
    donuts_weight = 0
    eaten_donuts = []
    sorted_donuts = sorted(
        donuts, key=operator.attrgetter('calories'))
    size = stomach.get_stomach_capacity()
    
    while size >= 0 and sorted_donuts:
        next_donut = sorted_donuts.pop()
        donut_weight = next_donut.get_weight()
        if size < donut_weight:
            continue
        size -= donut_weight
        eaten_calories += next_donut.get_calories()
        donuts_weight += donut_weight
        eaten_donuts.append(next_donut)
    
    for donut in eaten_donuts:
        print(repr(donut))
    print(f"Eaten calories: {eaten_calories}")
    print(f"Total weight: {donuts_weight}")


def donut_generator(how_many):
    """Function to generate as many donuts as given in how_many"""
    donuts = []
    for x in range(how_many):
        donuts.append(
            Donut(f.give_int(50, 250), f.give_int(150, 350), f.give_filling()))
    return donuts


stomach = Stomach(400)
donuts = donut_generator(20)
greedy_algorithm(donuts, stomach)
