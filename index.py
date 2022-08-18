


def niaveAlgo(a,b):
    best = 0
    for i in range(a+b):
        i+=1
        if a%i == 0 and b%i == 0:
            best = i
    return best



print(niaveAlgo(36,6))