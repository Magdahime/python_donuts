import algorithms as alg

def main():
    message = "This program will help you"
    message += " estimate which donuts you should eat "
    message += "based on their weight and calories!"
    stars = "*" * len(message)
    print(stars)
    print("Hello!")
    print(message)
    print(stars)
    quest = "Do you want to generate donuts(1) or input them manually(2)?: "
    answer = alg.get_int(1, 2, quest)
    if answer == 1:
        print("Generating donuts...")
        how_many = alg.get_int(1, 120, "How many donuts do you want?: ")
        donuts = alg.donut_generator(how_many)
        print(donuts)
    else:
        print("Answer 2")


main()