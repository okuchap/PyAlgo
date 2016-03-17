#Palindrome Checker
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def removeWhite(s):
    newStr = ""
    for ch in s:
        if ch != " " and ch != "\'": #特殊文字の扱い
            newStr = newStr + ch
    return newStr

def isPal(s):
    s = removeWhite(s)
    if s == reverse(s):
        return True
    else:
        return False

test = "radar"
print (isPal(test))