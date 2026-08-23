from collections import defaultdict

n_m = input().split()
n, m = int(n_m[0]), int(n_m[1])
group_a, group_b = [], []

for i in range(n):
    group_a.append(input())

for i in range(m):
    group_b.append(input())

a_positions = defaultdict(list)

# for i, val in enumerate(group_b):
#     if val in group_a:
#         answer_dict[val].append()
#     else:
#         answer_dict[val].append(-1)

for i, word in enumerate(group_a):
    a_positions[word].append(i+1)

answer_dict = defaultdict(list)

for word in group_b:
    answer_dict[word] = a_positions.get(word)
    

for word, indices in a_positions.items():    
    print(*indices)

print(a_positions)