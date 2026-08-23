# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S_k = input().split(" ")
S = S_k[0]
k = int(S_k[1])

permutated_list = list(permutations(S, k))

for i in range(1, len(permutated_list)):
    j = i - 1
    key = permutated_list[i]

    while j >= 0 and key < permutated_list[j]:
        permutated_list[j + 1] = permutated_list[j]
        j -= 1

    permutated_list[j + 1] = key

for permutation in permutated_list:
    print(*permutation, sep="")
