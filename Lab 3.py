def printMax(n1,n2):
    if n1 > n2:
        print n1
    else:
        print n2
        
def printMaxMin(n1,n2,n3):
    print 'max is'
    if n1 > n2 and n1 > n3:
        print n1
    elif n2 > n1 and n2 > n3:
        print n2
    elif n3 > n1 and n3 > n2:
        print n3
    print 'min is'
    if n1 < n2 and n1 < n3:
        print n1
    elif n2 < n1 and n2 < n3:
        print n2
    elif n3 < n1 and n3 < n2:
        print n3

def isEvenOrOdd(n1):
    if n1 % 2 == 0:
        print 'even'
    else:
        print 'odd'

def printMaxOfList():
    list = [23,34,54]
    print max(list)
    
printMaxOfList()
printMax(2,3)
printMaxMin(1,2,3)
isEvenOrOdd(3)