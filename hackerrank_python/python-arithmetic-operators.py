#problem :: 3 Arithmetic Operators

#solve :: 

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    if a > 0 and b > 0:
        if a < 10000000001 and b < 10000000001:
            print(a + b)
            print(a - b)
            print(a * b)
        
