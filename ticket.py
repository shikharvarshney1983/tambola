import random

def checkValid(lstNum, num, cnt):
    for i in range(0,71,10):
        if num >= i and num < i+10:
            count = 0
            for nm in lstNum:
               if nm >= i and nm < i+10:
                   count += 1 
            if count == cnt:
                return False
    if num >= 80 and num < 91:
        count = 0
        for nm in lstNum:
            if nm >= 80 and nm < 91:
                count += 1
        if count == cnt:
            return False
    return True
            

def retTicket():
    numbers = []

    numbers.append(random.sample(range(1,10),1)[0])
    for i in range(1,8):
        numbers.append(random.sample(range(i*10,i*10+10),1)[0])
    numbers.append(random.sample(range(80,91),1)[0])

    for i in range(0,6):
        chk = True
        while (chk):
            num = random.choice(list(set(range(1, 91))-set(numbers)))
            if checkValid(numbers, num, 3):
                numbers.append(num)
                chk = False
    
    numbers.sort()
    return numbers

def chkLstCount():
    pass

def getSingleNumLst(lstNum, linenum):
    ret = []
    lstNum.sort()
    for i in lstNum:
        if checkValid(ret, i, 1):
            ret.append(i)
    return ret   
    
def getLines(lstNum):
    ret = []
    for i in range (0,3):
        lst = []
        tmpLstNum = getSingleNumLst(lstNum)
        print("tmpLstNum = ",tmpLstNum)
        for j in range (0,5):
            nm = random.sample(tmpLstNum,1)[0]
            lst.append(nm)
            lstNum.remove(nm)
            tmpLstNum.remove(nm)
        lst.sort()
        print("lst = ",lst)
        ret.append(lst)
    return ret
            
numbers = retTicket()
print("numbers =" ,numbers)
lines = getLines(numbers)
print(lines)