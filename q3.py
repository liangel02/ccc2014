def geneva(s):
    m = 1
    q = []
    r = []
    k = len(s) -1
    while k >= 0:
        if s[k] == m:
            q.append(s[k])
            m = m + 1
            k = k - 1
        else:
            if len(r) != 0 and r[-1] == m:
                q.append(r[-1])
                del r[-1]
                m = m + 1
            else:
                r.append(s[k])
                k = k - 1
    for a in range(len(r)-1, -1, -1):
        if r[a] == m:
            q.append(r[a])
            m = m + 1
        else:
            return "N"
    return "Y"


test = int(input())

n = []
total = []

run = []

for i in range(test):
    N = int(input())
    n.append(N)
    for b in range(N):
        car = int(input())
        total.append(car)
c = 0
j = 0

for i in range(test):
    run = []
    for d in range(0, n[c], 1):
        run.append(total[j + d])
    j = j + n[c]
    temp = geneva(run)
    if temp == "N":
        print("N")
    else:
        print("Y")
    c = c + 1
