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
