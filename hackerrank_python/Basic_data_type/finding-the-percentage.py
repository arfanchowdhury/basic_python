#problem :: 11 finding the percentage

#solve ::

if __name__ == '__main__':
    N = int(input()) 
    dictionary = {} 
    for i in range(0, N): 
        inputArray = input().split()
        marks = list(map(float, inputArray[1:])) 
        dictionary[inputArray[0]] = sum(marks)/float(len(marks)) 
    print("%.2f" % dictionary[input()])

