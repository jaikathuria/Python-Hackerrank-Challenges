m = int(raw_input())
a = set(map(int,raw_input().split()))
n = int(raw_input())
b = set(map(int,raw_input().split()))
print len(a.union(b))