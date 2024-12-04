# Писать код сюда

from random import randint

def rand_nums():
    with open('numbers.txt', 'w') as f:
        for _ in range(1000):
            f.write(str(randint(1, 1000)) + ' ')


if __name__ == '__main__':
    pass
