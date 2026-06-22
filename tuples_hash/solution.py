if __name__ == '__main__':
    input()
    integer_list = map(int, input().strip().split(" "))
    print(hash(tuple(integer_list)))