markSheet = [[raw_input(),float(raw_input())] for _ in xrange(int(raw_input()))]
SecondLowScore = sorted(list(set(marks for name,marks in markSheet)))[1]
nameList = []
for _ in markSheet:
    if _[1] == SecondLowScore:
        nameList.append(_[0])
for name in sorted(nameList):
    print name
