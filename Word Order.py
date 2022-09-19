n = {}
k=int(input())

for i in range(k):
    j=input()
    count=1
    if j in n:
        n[j] += 1
    else:
        n[j]=1
print(len(n))
print(*n.values())