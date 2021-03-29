def deleteDigitFromList(TheList, sizeOfList, digit):
    newList = []
    STRdigit = str(digit)
    newList = deleteDigitFromList2(TheList, sizeOfList, STRdigit, newList)
    newList.reverse()
    return newList

def deleteDigitFromList2(TheList, sizeOfList, STRdigit, newList):
    if TheList == []:
        return newList
    TheList[sizeOfList-1] = str(TheList[sizeOfList-1])
    num = deleteDigitFromList2Rec(TheList[sizeOfList-1], STRdigit)
    num = int(num)
    newList.append(num)
    return deleteDigitFromList2(TheList[:sizeOfList - 1], sizeOfList - 1, STRdigit, newList)

def deleteDigitFromList2Rec(number, digit):
    if number =="":
        return 0
    if number.find(digit) == -1:
        return number
    x = number.find(digit)
    number = number[:x]+number[x+1:]
    return deleteDigitFromList2Rec(number, digit)


#        0   1   2    3    4  5     - all is 6
List = [123,410,111,12112,456,1]

#        0  1   2     - all is 3
LList = [1,123,212]
print(deleteDigitFromList(List,6,1))
#print("this is CS: " , List)
print(deleteDigitFromList(LList, 3, 1))
