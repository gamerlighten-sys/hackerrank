def get_all_substrings(string):
    substrings = []

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substrings.append(string[i:j])

    return substrings

def minion_game(string):
    substrings = get_all_substrings(string)
    vowels = ["a", "e", "i", "o", "u"]
    stuart_score, kevin_score = 0, 0
    
    for s in substrings:
        if s[0].lower() in vowels:
            kevin_score += 1
        else:
            stuart_score += 1

    if kevin_score > stuart_score:
        result = f"Kevin {kevin_score}"
    elif kevin_score == stuart_score:
        result = "Draw"
    else:
        result = f"Stuart {stuart_score}"

    print(result)

if __name__ == '__main__':
    s = input()
    minion_game(s)