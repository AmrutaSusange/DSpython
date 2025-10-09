import re
if __name__ == '__main__':
    with open('./para2.txt', 'r') as f:
        paragraph = f.read()
        paragraph1 = re.sub(r"(\w+)(?=\.)", 'is', paragraph )
        print(paragraph1)







