FIGURES_INPUT_DATA = [
    {"type": "square", "center_x": 0, "center_y": 0, "side": 2, "color": "black"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 100, "color": "red"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 200, "color": "blue"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 50, "color": "blue"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 100, "color": "red"}
]


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


def create_figures() -> list:
    return []


def main():
    print("Figures")


if __name__ == '__main__':
    main()
