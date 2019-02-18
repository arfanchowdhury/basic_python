#problem :: 9 find-second-maximum-number-in-a-list

#solve :: 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

