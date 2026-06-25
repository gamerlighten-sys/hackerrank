import textwrap

def wrap(string, max_width):
    wrapped_list = textwrap.wrap(string, max_width)
    wrapped_string = ""
    for i in range(len(wrapped_list)):
        wrapped_string += wrapped_list[i]
        wrapped_string += "\n"
    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)