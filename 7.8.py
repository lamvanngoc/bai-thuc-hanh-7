def d(ds,tep):
    mo=open(tep,'a+')
    mo.write(ds)
ds='abc'
d(ds,'python.txt')
mo=open('python.txt','r')
print(mo.read())
z