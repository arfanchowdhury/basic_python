#problem :: 12 python-lists

#solve ::

if __name__ == '__main__':
    N = int(input())
    L=[]
    
    for i in range(0, N):
        data = input().split()
        if data[0] == "insert":
            L.insert(int(data[1]), int(data[2]))
        elif data[0] == "append":
            L.append(int(data[1]))
        elif data[0] == "pop":
            L.pop()
        elif data[0] == "print":
            print(L)
        elif data[0] == "remove":
            L.remove(int(data[1]))
        elif data[0] == "sort":
            L.sort()
        else:
            L.reverse()

