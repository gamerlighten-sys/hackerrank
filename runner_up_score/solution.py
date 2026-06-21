if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    runner_up = -999999999
    
    for score in arr:
        if score > runner_up and score < max(arr):
            runner_up = score
    print(runner_up)