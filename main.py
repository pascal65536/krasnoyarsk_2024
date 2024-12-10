from random import randint


def summator():
    with open("numbers.txt", "r", encoding="utf8") as file:
        return sum(map(int, file.readline().split()))

def mult_nums():
    """
    help
    """
    with open('numbers.txt', encoding='utf-8') as f:
        data = f.read()
    nums = data.split()
    mult = 1
    for x in nums:
        mult *= int(x)
    return mult

def rand_nums():
    with open('numbers.txt', 'w') as f:
        for _ in range(1000):
            f.write(str(randint(1, 1000)) + ' ')

def mult_even_nums():
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        numbers = map(int, content.split())
        even_numbers = [num for num in numbers if num % 2 == 0]

        product = 1
        for num in even_numbers:
            product *= num

        return product if even_numbers else 0


if __name__ == '__main__':
    pass
