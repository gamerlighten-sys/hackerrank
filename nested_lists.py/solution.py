if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = []
    for name, score in records:
        scores.append(score)
        
    scores = list(set(scores))
    scores.sort()
    
    second_lowest = scores[1]
    names = []
    
    for name, score in records:
        if score == second_lowest:
            names.append(name)
   
    names.sort()
    print(*names, sep="\n")