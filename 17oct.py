class lipstick:

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"Object info: {self.color}"

    def __add__(self, other):
        v = self.color + other.color
        return lipstick(color=v)


if __name__ == '__main__':
    nayka_lipstick = lipstick('yellow')
    zara_lipstick = lipstick('magenta')

    print(nayka_lipstick)
    print(zara_lipstick)

    myntra_lipstick = nayka_lipstick + zara_lipstick

    print(myntra_lipstick)






