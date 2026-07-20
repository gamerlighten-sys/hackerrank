def minion_game(string):
    n = len(string)
    vowels = {"A", "E", "I", "O", "U"}
    stuart_score, kevin_score = 0, 0

    for i, ch in enumerate(string.upper()):
        # All substrings that start at index i contribute (n - i) points.
        points = n - i
        if ch in vowels:
            kevin_score += points
        else:
            stuart_score += points

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