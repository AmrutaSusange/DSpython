if __name__ == '__main__':

    with open('para.txt') as f:
        sentences = f.readlines()

    paragraph = ' '.join(sentences)
    print(paragraph)

    print(paragraph.split(' '))