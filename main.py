def multiple3() -> list[int]:
    with open('numbers.txt', 'r', encoding='utf8') as numbers:
        return [int(num) for num in numbers.read().split() if int(num) % 3 == 0]



if __name__ == '__main__':
    pass
