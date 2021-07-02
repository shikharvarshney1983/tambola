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

def chkLstCount(lstNum):
    lst=[0,0,0,0,0,0,0,0,0]
    retLst=[[],[],[],[],[],[],[],[],[]]
    for nm in lstNum:
        for i in range(0,71,10):
            if nm >= i and nm < i+10:
                lst[int(i/10)] = lst[int(i/10)] + 1
                retLst[int(i/10)].append(nm)
        if nm >= 80 and nm < 91:
            lst[8] = lst[8] + 1
            retLst[8].append(nm)
    return lst, retLst

def getSingleNumLst(lstNum):
    ret = []
    lstNum.sort()
    for i in lstNum:
        if checkValid(ret, i, 1):
            ret.append(i)
    return ret   

def createLinewithBlank(line):
    lst = ['','','','','','','','','']
    for i in line:
        index = int(i/10) if i != 90 else 8
        lst[index] = str(i)
    return lst
    
def getLines(lstNum):
    line1 = []
    line2 = []
    line3 = []
    val, lst = chkLstCount(lstNum)
    for i in range(0,9):
        if val[i] == 3:
            line1.append(lst[i][0])
            lstNum.remove(lst[i][0])
            line2.append(lst[i][1])
            lstNum.remove(lst[i][1])
            line3.append(lst[i][2])
            lstNum.remove(lst[i][2])
    tmpLstNum = getSingleNumLst(lstNum)
    for i in range(5 - len(line1)):
        nm = random.sample(tmpLstNum,1)[0]
        line1.append(nm)
        lstNum.remove(nm)
        tmpLstNum.remove(nm)
    val, lst = chkLstCount(lstNum)
    for i in range(len(val)):
        if val[i] == 2:
            line2.append(lst[i][0])
            lstNum.remove(lst[i][0])
            line3.append(lst[i][1])
            lstNum.remove(lst[i][1])
    for i in range(5-len(line2)):
        nm = random.sample(lstNum,1)[0]
        line2.append(nm)
        lstNum.remove(nm)
    for nm in lstNum:
        line3.append(nm)
    line1 = createLinewithBlank(line1)
    line2 = createLinewithBlank(line2)
    line3 = createLinewithBlank(line3)
    return [line1,line2,line3]

if __name__ == "__main__":
    numbers = retTicket()
    print("numbers =" ,numbers)
    lines = getLines(numbers)
    print(lines)