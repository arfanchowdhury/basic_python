
#problem :: 18 find-a-string

#solve ::

def count_substring(string, sub_string):
    total = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            total += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)