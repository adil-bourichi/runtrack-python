string = "abcdefghijklmnopqrstuvwxyz"*10
n=1
i=0
Stop=False
while i< len(string):
    for j in range(n):
        if i<len(string):
            print(string[i],end='')
            i+=1
        else:
            Stop=True
            break
    print()
    n+=1

