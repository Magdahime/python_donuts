import functions as f
from donut import Donut
from stomach import Stomach
import operator


def greedy_algorithm(donuts, stomach):
    print("\nGREEDY ALGORITHM: \n")
    eaten_calories = 0
    donuts_weight = 0
    eaten_donuts = []
    sorted_donuts = sorted(
        donuts, key=operator.attrgetter('value_ratio'))
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


def donutbox(size, weight_tab, calories_tab, donuts_num):
    if donuts_num == 0 or size == 0:
        return 0
    if weight_tab[donuts_num-1] > size:
        return donutbox(size, weight_tab, calories_tab, donuts_num-1)
    else:
        return (
            max(calories_tab[donuts_num-1] + donutbox(size - weight_tab[donuts_num-1], weight_tab, calories_tab, donuts_num-1),
                donutbox(size, weight_tab, calories_tab, donuts_num-1)))


def recursive_solution(donuts, stomach):
    print("\nRECURSIVE METHOD: \n")
    weight_tab = [donut.get_weight() for donut in donuts]
    calories_tab = [donut.get_calories() for donut in donuts]
    donuts_num = len(calories_tab)
    size = stomach.get_stomach_capacity()
    eaten_calories = donutbox(size, weight_tab, calories_tab, donuts_num)
    
    print(f"Eaten calories: {eaten_calories}")
    

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
recursive_solution(donuts, stomach)
