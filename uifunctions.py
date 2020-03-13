import algorithms as alg


def print_greeting():
    greeting = "Hello!\n"
    greeting += "This program will help you"
    greeting += " choose which donuts you should eat "
    greeting += "based on their weight and calories!"
    stars = "*" * len(greeting)
    print(stars)
    print(greeting)
    print(stars)


def print_options():
    prompt = "What do you want to do now? We have plenty of options: "
    stars = "*" * len(prompt)
    print(stars)
    print(prompt)
    print("1. Show me donuts")
    print("2. Generate another set of donuts")
    print("3. Use recursive algorithm")
    print("4. Use greedy algorithm")
    print("5. Use dynamic algorithm")
    print("6. Measure time of chosen algorithm")
    print("7. Save to file")
    print("8. Get data from file")
    return "Answer: __"


def one(donuts):
    for donut in donuts:
        print(donut)


def two():
    prompt = "How many donuts you want to generate: "
    how_many = alg.get_int(1, 120, prompt)
    return alg.donut_generator(how_many)


def three(donuts, stomach):

    alg.recursive_solution(donuts, stomach)

