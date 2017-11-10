class Figure:
    def __init__(self, center_x: int, center_y: int):
        self.center_x = center_x
        self.center_y = center_y

        # def print_info(self):
        #     print("Figure center: ({}, {})".format(self.center_x, self.center_y))

    def __str__(self):
        return "Figure center: ({}, {})".format(self.center_x, self.center_y)

    def draw(self, canvas):
        print("Drawing figure {} on canvas".format(self))


class Circle (Figure):
    def __init__(self, center_x: int, center_y: int, radius: int):
        super().__init__(center_x, center_y)
        self.radius = radius

    def draw(self, canvas):
        print("Drawing circle OOOO")






figure1 = Figure(center_x=15, center_y=23)
circle1 = Circle(center_x=5, center_y=53, radius=12)
##print(figure1.print_info())

# print(figure1)
figure1.draw(None)
circle1.draw(None)
print(circle1)

