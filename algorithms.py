from timeit import default_timer as timer
from donut import Donut
from stomach import Stomach
import operator
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
    return int(number)


def print_list(list1):
    for x in range(len(list1)):
        for y in range(len(list1[x])):
            print(str(list1[x][y]), end=" ")
        print("\n")


def algorithm_des(algorithm_name, eaten_calories, donuts_weight=0, donuts=[]):
    """Helps describe results of an algorithm"""
    stars = "*" * len(algorithm_name)
    print(stars)
    print(algorithm_name.upper())
    print(stars)
    if donuts and donuts_weight:
        print("Eaten donuts:")
        for donut in donuts:
            print(donut)
        print(f"Total weight: {donuts_weight}")
    print(f"Eaten calories: {eaten_calories} \n")


def time_test_des(algorithm_name, iterations, elapsed_time):
    """Helps describe result of time test"""
    message = "Time of repeating " + algorithm_name + " algorithm "
    message += str(iterations) + " times:"
    stars = "*" * len(message)
    print(stars)
    print(message)
    print(elapsed_time)
    print(stars + "\n")


def greedy_solution(donuts, stomach):
    sorted_donuts = sorted(
        donuts, key=operator.attrgetter('value_ratio'))
    size = stomach.get_stomach_capacity()

    eaten_donuts, eaten_calories, donuts_weight = greedy_algorithm(size, sorted_donuts)
    algorithm_des("greedy algorithm",
                    eaten_calories, donuts_weight, eaten_donuts)


def greedy_algorithm(size, sorted_donuts):
    '''Part of greedy algorithm responsible for calculating the result'''
    eaten_calories = 0
    donuts_weight = 0
    eaten_donuts = []
    while size >= 0 and sorted_donuts:
        next_donut = sorted_donuts.pop()
        donut_weight = next_donut.get_weight()
        if size < donut_weight:
            continue
        size -= donut_weight
        eaten_calories += next_donut.get_calories()
        donuts_weight += donut_weight
        eaten_donuts.append(next_donut)

    return eaten_donuts, eaten_calories, donuts_weight


def recursive_algorithm(size, weight_tab, calories_tab, donuts_num):
    if donuts_num == 0 or size == 0:
        return 0
    if weight_tab[donuts_num-1] > size:
        return recursive_algorithm(size, weight_tab, calories_tab, donuts_num-1)
    else:
        return (
            max(calories_tab[donuts_num-1] + recursive_algorithm(size - weight_tab[donuts_num-1], weight_tab, calories_tab, donuts_num-1),
                recursive_algorithm(size, weight_tab, calories_tab, donuts_num-1)))


def recursive_solution(donuts, stomach):
    
    weight_tab = [donut.get_weight() for donut in donuts]
    calories_tab = [donut.get_calories() for donut in donuts]
    donuts_num = len(calories_tab)
    size = stomach.get_stomach_capacity()
    eaten_calories = recursive_algorithm(size, weight_tab, calories_tab, donuts_num)
    algorithm_des("recursive algorithm", eaten_calories)


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
    return solution_matrix[donuts_num][size], chosen_donuts


def dynamic(size, weight_tab, calories_tab, donuts_num):
    solution, chosen_donuts = dynamic_algorithm(size, weight_tab, calories_tab, donuts_num)
    donuts_indexes = []
    free_space = size
    for i in range(donuts_num, 0, -1):
        if chosen_donuts[i][free_space] == 1:
            donuts_indexes.append(i)
            free_space -= weight_tab[i-1]
    total = size - free_space
    donuts_indexes.sort()
    donuts_indexes = [x-1 for x in donuts_indexes]

    return solution, donuts_indexes, total


def dynamic_solution(donuts, stomach):

    weight_tab = [donut.get_weight() for donut in donuts]
    calories_tab = [donut.get_calories() for donut in donuts]
    size = stomach.get_stomach_capacity()
    donuts_num = len(donuts)
    eaten_calories, donut_indexes, total = dynamic(size, weight_tab, calories_tab, donuts_num)
    eaten_donuts = [donuts[i] for i in donut_indexes]
    algorithm_des("dynamic algorithm", eaten_calories, total, eaten_donuts)


def donut_generator(how_many):
    '''Function to generate as many donuts as given in how_many'''
    donuts = []
    for x in range(how_many):
        donuts.append(
            Donut(give_int(30, 100), give_int(150, 350), give_filling()))
    return donuts


def get_parameters(stomach_size, how_many):

    stomach = Stomach(stomach_size)
    donuts = donut_generator(how_many)
    weight_tab = [donut.get_weight() for donut in donuts]
    calories_tab = [donut.get_calories() for donut in donuts]
    donuts_num = len(calories_tab)
    size = stomach.get_stomach_capacity()
    sorted_donuts = sorted(
        donuts, key=operator.attrgetter('value_ratio'))
    return donuts, weight_tab, calories_tab, donuts_num, size, sorted_donuts


def measure_time(func,  iterations,
                 size, weight_tab, calories_tab, donuts_num, sorted_donuts=[]):
    elapsed_time = 0
    if func == greedy_algorithm:
        greedy_start = timer()
        for x in range(iterations):
            func(size, sorted_donuts)
        greedy_end = timer()
        elapsed_time = greedy_end - greedy_start
    else:
        algorithm_start = timer()
        for x in range(iterations):
            func(size, weight_tab, calories_tab, donuts_num)
        algorithm_end = timer()
        elapsed_time = algorithm_end - algorithm_start
    return elapsed_time


def gather_information(algorithm, max_size, min_size, how_many, iterations):

    if algorithm == "greedy":
        func = greedy_algorithm
    elif algorithm == "recursive":
        func = recursive_algorithm
    else:
        func = dynamic_algorithm

    results = []
    stomach_sizes = []
    param = get_parameters(min_size, how_many)
    (donuts, weight_tab, calories_tab, donuts_num, size, sorted_donuts) = param
    while size <= max_size:
        stomach_sizes.append(size)
        result = measure_time(func, iterations, size, weight_tab,
                      calories_tab, donuts_num, sorted_donuts)
        results.append(round(result, 6))
        size += 20
    return results, stomach_sizes

