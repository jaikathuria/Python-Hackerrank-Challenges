m = int(raw_input())
mSet = set(map(int,raw_input().split()))
n = int(raw_input())
nSet = set(map(int,raw_input().split()))
diff = sorted(list((nSet.union(mSet)).difference(nSet.intersection(mSet))))
for _ in diff:
    print _
