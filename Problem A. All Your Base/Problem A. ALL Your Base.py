e=open('E:/entrer2.txt','r')
s=open('E:/sorter2.txt','w')
n=int(e.readline())
for i in range(1,n+1):
    N=e.readline().replace('\n','')
    D=[]
    for j in N:
        if j not in D:
           D.append(j)
    sm=0
    if len(D)<2:p=2
    else:p=len(D)
    b=1
    for j in N[::-1]:
        y=D.index(j)
        if y==0:y=1
        elif y==1:y=0
        sm+=y*b
        b=b*p
    s.write('Case #%d: %d\n'%(i,sm))
e.close()
s.close()
