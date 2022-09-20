# Enter your code here. Read input from STDIN. Print output to STDOUT
m=input()
l=input().split()
a=set(input().split())
b=set(input().split())
count=0
for i in l:
    if i in a:
        count=count+1
    if i in b:
        count=count-1
print(count)
