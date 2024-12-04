from math import sqrt

def maxsqr():
    f = open('numbers.txt', encoding='utf-8')
    data = f.readline()
    data = data.split(' ')
    maxNum = 0
    for j in data:
        number = sqrt(int(j))
        if number.is_integer() and maxNum < int(j):
            maxNum = int(j)
    f.close()
    return maxNum

def minever():
    f = open('numbers.txt', 'r', encoding='utf8')
    lines = f.read().split()
    minnum = int(lines[0])
    recnum = 0
    for i in lines:
        if int(i) < minnum and int(i) % 2 == 0:
            minnum = int(i)
    if minnum % 2 == 0:
        recnum = minnum
    else:
        print('Таких чисел нет')
    f.close()


def multiply() -> int:
    s = 1
    with open('numbers.txt').read().split(' ') as a:
        for i in a:
            s *= i
    return s 	

def summa() -> int:
    summ = 0
    with open('numbers.txt', 'r') as file:
        summ = sum(map(int, file.readlines()[0].rstrip().split()))
    
    return summ


def create() -> None:
    """
    Функция создания файла с простыми числами до 500 (Все числа записаны через пробел)
    Args:
        None
    Retuns:
        None
    """
    with open("numbers.txt", "w") as file:
        prime_numbers = []
        mini = [0] * 501
        for i in range(2, 501):
            if mini[i] == 0:
                mini[i] = i
                prime_numbers.append(i)
            for y in prime_numbers:
                if y * i > 500 or mini[i] < y:
                    break
                mini[y * i] = y

        prime_numbers = list(map(str, prime_numbers))
        file.write(" ".join(list(map(str, prime_numbers))))

