#Converting an Integer to a string in any base

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    #base case
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))