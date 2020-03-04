import functions as f


class Donut():
    """Class that will represent a donut"""
    def __init__(self, weight, calories, filling):
        self.filling = filling
        self.calories = calories
        self.weight = weight

    def __repr__(self):
        repr = f"Filling: {self.filling}\n"
        repr += f"Calories: {self.calories}\n"
        repr += f"Weight: {self.weight}\n"
        return repr

    def __str__(self):
        return f"A delicious donut with {self.filling} filling! Yummy!"

    def get_weight(self):
        return self.weight

    def get_calories(self):
        return self.calories


def test1():
    print("Constructing a box of donuts:")
    box_of_donuts = []
    for x in range(10):
        box_of_donuts.append(
            Donut(f.give_int(50, 250), f.give_int(150, 350), f.give_filling()))
    for donut in box_of_donuts:
        print(donut)
