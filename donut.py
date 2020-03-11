class Donut():
    """Class that will represent a donut"""
    def __init__(self, weight, calories, filling):
        self.filling = filling
        self.calories = calories
        self.weight = weight
        self.value_ratio = calories/weight

    def __str__(self):
        donut = f"Filling: {self.filling}\n"
        donut += f"Calories: {self.calories}\n"
        donut += f"Weight: {self.weight}\n"
        return donut

    def get_weight(self):
        return self.weight

    def get_calories(self):
        return self.calories
