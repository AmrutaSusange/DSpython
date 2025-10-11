class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self  # the object itself is the iterator

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

class abc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.b:
            raise StopIteration
        value = self.a
        self.a += 1
        return value

if __name__ == "__main__":

    with open('para3.txt') as f:
        paragraph = f.read()

    import re
    import string

    clean_paragraph = re.sub(f'[{re.escape(string.punctuation)}]', '', paragraph)
    paragraph = re.sub('\s{2,}', ' ', clean_paragraph).strip()

    text = "8343"

    cond1 = text.isdigit()
    cond2 = text.isalpha()


    print(all([cond1, cond2]))

    class a:
        def __int__(self):
            print('dsfds')

    xx = a()

    print(isinstance("dsfsdf", xx))




