n,m = map(int,raw_input().split())
arr = map(int,raw_input().split())
a = set(map(int,raw_input().split()))
b = set(map(int,raw_input().split()))
happy = 0
for _ in arr:
    if _ in a:
        happy += 1
    if _ in b:
        happy -= 1
print happy
