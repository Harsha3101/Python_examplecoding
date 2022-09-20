if __name__ == '__main__':

    N = int(input())
    k=[]
    for i in range(N):
        m=input().split()
        if m[0] == 'insert':
            k.insert(int(m[1]),int(m[2]))
        elif m[0] == 'append':
            k.append(int(m[1]))
        elif m[0] == 'remove':
            k.remove(int(m[1]))
        elif m[0] == 'pop':
            k.pop()
        elif m[0] == 'reverse':
            k.reverse()
        elif m[0] == 'sort':
            k.sort()
        else:
            print(k)