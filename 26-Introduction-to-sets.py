from __future__ import division

def average(array):
    array = list(set(array))
    return sum(array)/len(array)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
