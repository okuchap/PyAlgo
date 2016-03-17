#DP Exercises

'''
#Ex.1
def fact(n):
    #n is a natural number. Return the factorial of n.
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def main():
    num = 5
    print(fact(num))

main()
'''

#Ex.2
def reverseList(list):
    #Base case
    if len(list) == 1:
        return list
    #Step case
    else:
        return [list[len(list)-1]] + reverseList(list[0:len(list)-1])


#Ex.6 Tower of Hanoi???
def timesOfHanoi(n):
    #n is the number of disks
    if n == 1:
        return 1
    else:
        return 2*timesOfHanoi(n-1)+1

def moveTower(height,from,to,with):
    moveTower(height-1,from,with,to)
    print("moving disk from",from,"to",to)
    moveTower(height-1,with,to,from)

#Ex.13 Pascal's Triangle

from math import factorial
def calcCoef(n,k):
    if k == 0 or k == n:
        return 1
    elif 1<=k and k<=n-1:
        return calcCoef(n-1,k)+calcCoef(n-1,k-1)

def drawPascal(n):
    for k in range(n+1): #k is the row number
        for j in range(k+1):
            if j != k:
                print(calcCoef(k,j), end=" ")
            else:
                print(calcCoef(k,j))





