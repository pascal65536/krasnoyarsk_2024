from math import sqrt


primelist = [11, 13, 17, 19, 23, 27]
for i in range(500):
    for p in primelist:
        if not i % p:
            continue   
    print(i, end=' ')
print()

def maxsqr():
    f = open('numbers.txt', encoding='utf-8')
    data = f.readlines()
    maxNum = 0
    for j in data:
        j = j.replace('\n', '')
        number = sqrt(int(j))
        if number.is_integer() and maxNum < int(j):
            maxNum = int(j)
    f.close()
    return maxNum