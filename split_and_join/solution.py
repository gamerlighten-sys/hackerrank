def split_and_join(line:str):
    words = line.split(" ")
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)