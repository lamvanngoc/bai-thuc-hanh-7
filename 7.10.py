file=open('python.txt','r')
ds=[]
if file.mode=='r':
    data=file.readlines()
    for line in data:
        ds.append(line.split())
print(ds)
dst=[]
for i in ds:
    dst.extend(i)
print(dst)
dsdai=[]
for i in range(0,len(dst)):
    dsdai.append(len(dst[i]))
print(dsdai)
for i in dst:
    if len(i)==max(dsdai):
        print('tu dai nhat laf:',i)
