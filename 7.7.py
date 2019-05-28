mo=open('python.txt','r')
d=0
for c in mo:
    for i in range(0,len(c)):
        if c[i]=='\n':
            d=d+1
print(d)