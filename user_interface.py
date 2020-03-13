from stomach import Stomach
import algorithms as alg
import uifunctions as ui


def main():
    try:
        ui.print_greeting()
        quest = "Do you want to generate donuts(1) or input them manually(2)?: "
        answer = alg.get_int(1, 2, quest)
        if answer == 1:
            how_many = alg.get_int(1, 120, "How many donuts do you want?: ")
            print("\n\nGenerating donuts...\n\n")
            donuts = alg.donut_generator(how_many)
            stomach_size = alg.get_int(100, 400, "How big is your stomach?(grams): ")
            stomach = Stomach(stomach_size)
            answer = alg.get_int(1, 8, ui.print_options())
            
            
        else:
            print("Answer 2")
    except KeyboardInterrupt:
        exit()


main()