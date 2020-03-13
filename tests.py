import algorithms as alg
from timeit import default_timer as timer
from donut import Donut
from stomach import Stomach


def algorithm_test():
    stomach = Stomach(400)
    donuts = alg.donut_generator(20)
    alg.greedy_solution(donuts, stomach)
    alg.recursive_solution(donuts, stomach)
    alg.dynamic_solution(donuts, stomach)


def time_test(stomach_size, how_many, iterations):

    param = alg.get_parameters(stomach_size, how_many)
    (donuts, weight_tab, calories_tab, donuts_num, size, sorted_donuts) = param
    greedy = alg.measure_time(alg.greedy_algorithm, iterations, size,
                              weight_tab, calories_tab, donuts_num, sorted_donuts)
    alg.time_test_des("greedy", iterations, greedy)

    recursive = alg.measure_time(alg.recursive_algorithm, iterations, size,
                                 weight_tab, calories_tab, donuts_num)
    alg.time_test_des("recursive", iterations, recursive)

    dynamic = alg.measure_time(alg.dynamic_algorithm, iterations, size,
                               weight_tab, calories_tab, donuts_num)
    alg.time_test_des("dynamic", iterations, dynamic)


def test1():
    print("Constructing a box of donuts:")
    box_of_donuts = []
    for x in range(10):
        box_of_donuts.append(
            Donut(alg.give_int(50, 250), alg.give_int(150, 350), alg.give_filling()))
    for donut in box_of_donuts:
        print(donut)


test1()
time_test(100, 20, 20)