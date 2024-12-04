def summa() -> int:
    summ = 0
    with open('numbers.txt', 'r') as file:
        for line in file.readlines():
            summ += int(line.rstrip())
    
    return summ


print(summa())