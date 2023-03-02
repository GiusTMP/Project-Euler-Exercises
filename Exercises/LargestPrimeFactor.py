def es(n):
    i = ""
    quoto = n
    div = 2
    while True:
        while quoto % div != 0:
            div += 1
        if quoto // div == 1:
            i += str(div) + ' '
            l = list(map(int,i.rstrip().split(' ')))
            return max(l)
        else:
            quoto = quoto // div
            i += str(div) + ' '
            div = 2
print(es(600851475143))   