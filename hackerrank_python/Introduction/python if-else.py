#problem :: 2 python if-else

#solve ::


if __name__ == '__main__':
    n = int(input())
    if n > 0 and n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n in range(2,5):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6,20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    elif n % 2 == 0 and n in range(20,100):
        print("Weird")


    