def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
             p = i
             for j in range(len(sub_string)):
                if p > len(string) - 1:    
                    return count
                if string[p] == sub_string[j]:
                    p += 1
                    if j == len(sub_string) - 1:
                        count += 1                       
                else:
                    break      
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)