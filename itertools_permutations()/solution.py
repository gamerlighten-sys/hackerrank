from itertools import permutations

S, K = input(), int(input())

print(list(permutations(S, K)))
