def mult_nums():
    with open('numbers.txt', encoding='utf-8') as f:
        data = f.read()
    nums = data.split()
    mult = 1
    for x in nums:
        mult *= int(x)
    return mult
# Писать код сюда