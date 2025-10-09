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
        word = f.read()


    import re
    import string


    word = re.sub(f"[{re.escape(string.punctuation)}]", " ", word)

    l = re.sub("\s{2,}", " ", word).strip().split(' ')
    d = {k:v for k,v in enumerate(l)}
    print(d)

    print(string.punctuation)

    # for i,j in enumerate(iterable):
    #     text_dict[i] = [j]
    # print(text_dict)



