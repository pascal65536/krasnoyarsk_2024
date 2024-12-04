primelist = [11, 13, 17, 19, 23, 27]
for i in range(500):
    for p in primelist:
        if not i % p:
            continue   
    print(i, end=' ')
print()

