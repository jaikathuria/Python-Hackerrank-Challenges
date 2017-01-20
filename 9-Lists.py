if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(N):
        _ = input().split()
        cmd = _[0]
        arg = _[1:]
        if cmd == "print":
            print(List)
        else:
            eval("List." + cmd + "(" + (",".join(arg)) + ")")
      
