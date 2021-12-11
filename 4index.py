#task 5

def calcBetween(a, b):
    acc = 0
    for i in range(a + 1, b):
        acc += 1
    return acc

print(calcBetween(10, 15))
