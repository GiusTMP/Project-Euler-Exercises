def es(n):
    somma = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            somma += i
    return somma

print(es(1000))
            