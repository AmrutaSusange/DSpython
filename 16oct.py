import random

class african:
    africa = True

class animal:
    alive = True

class human(animal):
    has_eyes = True
    has_legs = True
    has_hands = True
    has_nose = True
    has_brain = True
    has_backbone = True

    count_of_all_human = 0
    height = 10

class employee(human,african):

    def __init__(self, born_in_country, father, mother, gender):
        human.count_of_all_human += 1
        human.height -= 1
        self.h = random.randint(3, human.height)
        self.born_in_country = born_in_country
        self.father_name = father
        self.mother_name = mother
        self.gender = gender

    def __repr__(self):
        return f"""
        Person 
        gender: {self.gender}
        father: {self.father_name}
        mother: {self.mother_name}
        born place: {self.born_in_country}
        height: {self.h}
        """


if __name__ == "__main__":
    sudhir = employee("delhi", "ram", "prabila", "M")
    amruta = employee("pune", "ram", "kishori", "F")
    parvati = employee("andamand", "bablu", "christina", "F")

    print(sudhir.africa)
