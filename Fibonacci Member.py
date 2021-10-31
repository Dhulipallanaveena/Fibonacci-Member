import math
def isPerfectSquare(n):
    s=int(math.sqrt(n))
    return s*s==n
def checkMember(n):
    return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
    

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
