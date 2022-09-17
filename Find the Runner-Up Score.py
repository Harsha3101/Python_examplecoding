if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m=sorted(list(set(arr)))
    print(m[-2])
