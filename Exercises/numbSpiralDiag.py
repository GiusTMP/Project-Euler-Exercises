
import math
def numbSpiralDiag(n):
    somma = 1
    dimLato = 3
    while dimLato <= n:
        nFirst = math.pow(dimLato,2)
        somma += nFirst
        for i in range(3):
            nFirst = nFirst - (dimLato - 1)
            somma += nFirst
        dimLato += 2
    return somma

print(numbSpiralDiag(1001))
            
    
        