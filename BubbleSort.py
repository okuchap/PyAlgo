#bubble sort
def bubblesort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i+1] = alist[i]
                alist[i+1] = temp

#short bubble
def shortBubble(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum >= 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1