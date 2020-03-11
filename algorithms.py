import functions as f
from timeit import default_timer as timer
from donut import Donut
from stomach import Stomach
import operator


def greedy_solution(donuts, stomach):
    sorted_donuts = sorted(
        donuts, key=operator.attrgetter('value_ratio'))
    size = stomach.get_stomach_capacity()

    eaten_donuts, eaten_calories, donuts_weight = greedy_algorithm(size, sorted_donuts)
    f.algorithm_des("greedy algorithm",
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
    f.algorithm_des("recursive algorithm", eaten_calories)


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
    f.algorithm_des("dynamic algorithm", eaten_calories, total, eaten_donuts)


def donut_generator(how_many):
    '''Function to generate as many donuts as given in how_many'''
    donuts = []
    for x in range(how_many):
        donuts.append(
            Donut(f.give_int(30, 100), f.give_int(150, 350), f.give_filling()))
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


def algorithm_test():
    stomach = Stomach(400)
    donuts = donut_generator(20)
    greedy_solution(donuts, stomach)
    recursive_solution(donuts, stomach)
    dynamic_solution(donuts, stomach)


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


def time_test(stomach_size, how_many, iterations):

    param = get_parameters(stomach_size, how_many)
    (donuts, weight_tab, calories_tab, donuts_num, size, sorted_donuts) = param
    greedy = measure_time(greedy_algorithm, "greedy", iterations, size,
                          weight_tab, calories_tab, donuts_num, sorted_donuts)
    f.time_test_des("greedy", iterations, greedy)

    recursive = measure_time(recursive_algorithm, "recursive", iterations, size,
                             weight_tab, calories_tab, donuts_num)
    f.time_test_des("recursive", iterations, recursive)

    dynamic = measure_time(dynamic_algorithm, "dynamic", iterations, size,
                           weight_tab, calories_tab, donuts_num)
    f.time_test_des("dynamic", iterations, dynamic)


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
        results.append(round(result, 4))
        size += 10
    return results, stomach_sizes


gather_information("dynamic", 400, 100, 60, 100)
        