# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
for i in range(k):

    n = int(input())
    l = input().split()
    condition = 'Yes'
    for j in range(int(n // 2)):
        if max(int(l[j]), int(l[-j - 1])) < min(int(l[j + 1]), int(l[-j - 2])):
            condition = 'No'
    print(condition)
