# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
money_earned = 0

for i in range(X):
    shoes = input().split(" ")

N = int(input())

for i in range(N):
    shoe_price = Counter(input().split())
    if shoe_price.keys() in shoes:
        shoes.remove(shoe_price.keys())
        money_earned += shoe_price.values()

print(money_earned)