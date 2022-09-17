# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
k=int(input())
Class = namedtuple('Class',list(map(str,input().split())))
marks=0
for i in range(k):
    strn=input().split()
    ma=Class(*strn)
    marks += int(ma.MARKS)
print(marks/k)