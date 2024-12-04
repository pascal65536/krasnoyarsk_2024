def summator():
    with open("numbers.txt", "r", encoding="utf8") as file:
        return sum(map(int, file.readline().split()))
