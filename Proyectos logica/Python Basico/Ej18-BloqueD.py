def media(*args):

    total = 0
    totalNums = 0
    for n in args:
        total += n
        totalNums += 1
    return total / totalNums

print(f"Media: {media(6,7,8)}")