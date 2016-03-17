#Stack Frames: Implementing Recursion

rStack = Stack()

def toStr(n, base):
    #n is an integer

    convertString = "0123456789ABCDEF"

    #Convert the given integer to the stack, using the given base
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base


    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))

