def solve(s):
    s_list = s.split(" ")
    new_s = ""
    for item in s_list:
        new_s += item.capitalize()
        new_s += " "
    return new_s
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
    
    s = input()
    print(solve(s))