# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
strings = [input() for _ in range(n)]
k = int(input())
mydict = dict()
for str1 in strings:
    if str1 in mydict:
        mydict[str1] +=1
    else:
        mydict[str1] = 1

cnt = 0
print(mydict)
for key,val in mydict.items():
    if val == 1:
        cnt+=1
        if cnt==k:
            print(key)