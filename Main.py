freq={}
def frequency(x):
    global freq
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    return freq
a=input()
for i in a:
    frequency(i)
def matrix(dictionary):
    count=0
    print("    ",end="")
    l=list(dictionary.keys())
    for i in l:
        print(i,end="   ")
    print("")
    print("")
    for j in range(len(l)):
        print(l[count],end="   ")
        for i in l:
            if i==l[count]:
                print(dictionary[i],end="   ")
            else:
                print("0",end="   ")
        print("")
        print("")
        count+=1
matrix(freq)
    
