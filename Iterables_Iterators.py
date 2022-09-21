# Enter your code here. Read input from STDIN. Print output to STDOUTimport math
import math
Size = int(input())
Cnt = len(list(filter(lambda x: x == "a", input().split())))
K = int(input())

total = math.comb(Size, K)
withoutA = math.comb(Size - Cnt, K)
result = 1 - withoutA / total
print("{0:.3f}".format(result))
