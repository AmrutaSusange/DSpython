if __name__ == "__main__":
    import random
    import string


    id = ''.join(random.sample(list(set(string.printable) - set(['\n', '\t', '\r', '\x0b', '\x0c', '\\'])), 9))
    print(id)