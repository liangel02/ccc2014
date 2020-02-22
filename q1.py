def invite(inList, outList, n):
    for m in range(len(inList)):
        if (m+1) % n != 0:
            outList.append(inList[m])


totalNum = int(input())
numOfRounds = int(input())

removeMultiples = []
numOfFriends = 1
listOfFriends = [1]
tempFriends = []

for i in range(numOfRounds):
    multiple = int(input())
    removeMultiples.append(multiple)

for i in range(1, totalNum, 1):
    numOfFriends = numOfFriends + 1
    listOfFriends.append(numOfFriends)

for i in range(len(removeMultiples)):
    invite(listOfFriends, tempFriends, removeMultiples[i])
    listOfFriends = tempFriends
    tempFriends = []

for i in range(len(listOfFriends)):
    print(listOfFriends[i])
