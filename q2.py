numOfStudents = int(input())
order1 = input()
order2 = input()

order1 = order1.split(" ")
order2 = order2.split(" ")

for i in range(len(order1)):
    if order1[i] == order2[i]:
        print("bad")
        exit()
    else:
        for p in range(len(order2)):
            if order1[i] == order2[p]:
                if order1[p] == order2[i]:
                    break
                else:
                    print("bad")
                    exit()
print("good")
