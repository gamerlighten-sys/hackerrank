def mutate_string(string, position, character):
    letter_list = list(string)
    letter_list[position] = character
    string = ""
    for letter in letter_list:
        string += letter
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)