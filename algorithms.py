import functions as f
from donut import Donut
from stomach import Stomach
import operator


def greedy_algorithm(donuts, stomach):
    method = "GREEDY METHOD:"
    print("*" * len(method))
    print(method)
    print("*" * len(method))
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
    method = "RECURSIVE METHOD:"
    print("*" * len(method))
    print(method)
    print("*" * len(method))
    weight_tab = [donut.get_weight() for donut in donuts]
    calories_tab = [donut.get_calories() for donut in donuts]
    donuts_num = len(calories_tab)
    size = stomach.get_stomach_capacity()
    eaten_calories = donutbox(size, weight_tab, calories_tab, donuts_num)

    print(f"Eaten calories: {eaten_calories}")


def dynamic_algorithm(size, weight_tab, calories_tab, donuts_num):
    solution_matrix = [[0 for x in range(size+1)] for x in range(donuts_num+1)]
    chosen_donuts = [[0 for x in range(size+1)] for x in range(donuts_num+1)]
    #d stands for donuts g for grams in size
    for d in range(donuts_num+1):
        for g in range(size+1):
            curr_w = weight_tab[d-1]
            curr_c = calories_tab[d-1]
            if curr_w <= g and (curr_c + solution_matrix[d-1][g - curr_w] > solution_matrix[d-1][g]):
                solution_matrix[d][g] = curr_c + solution_matrix[d-1][g - curr_w]
                chosen_donuts[d][g] = 1
            else:
                solution_matrix[d][g] = solution_matrix[d-1][g]
    donuts_indexes = []
    free_space = size
    for i in range(donuts_num, 0, -1):
        if chosen_donuts[i][free_space] == 1:
            donuts_indexes.append(i)
            free_space -= weight_tab[i-1]
    donuts_indexes.sort()
    donuts_indexes = [x-1 for x in donuts_indexes]
    
    return solution_matrix[donuts_num][size], donuts_indexes


def dynamic_solution(donuts, stomach):
    method = "DYNAMIC PROGRAMMING METHOD:"
    print("*" * len(method))
    print(method)
    print("*" * len(method))
    weight_tab = [donut.get_weight() for donut in donuts]
    calories_tab = [donut.get_calories() for donut in donuts]
    size = stomach.get_stomach_capacity()
    donuts_num = len(donuts)
    eaten_calories, donut_indexes = dynamic_algorithm(size, weight_tab, calories_tab, donuts_num)
    eaten_donuts = [donuts[i] for i in donut_indexes]
    print("EATEN DONUTS:\n")
    for donut in eaten_donuts:
        print(repr(donut))
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
weight_tab = [donut.get_weight() for donut in donuts]
calories_tab = [donut.get_calories() for donut in donuts]
donuts_num = len(calories_tab)
size = stomach.get_stomach_capacity()
greedy_algorithm(donuts, stomach)
recursive_solution(donuts, stomach)
dynamic_solution(donuts, stomach)