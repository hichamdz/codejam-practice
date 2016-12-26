e=open('E:/entrer2.txt','r')
s=open('E:/sorter2.txt','w')
def compare(x,y):
    if (x[0]>y[0] and x[1]>y[1]):
       return 1
    else:return 0
def compare2(x,y):
    if (x[0]<y[0] and x[1]<y[1]):
       return 1
    else:return 0
T=int(e.readline())
for i in xrange(1,T+1):
    N=int(e.readline())
    w=[]
    for j in xrange(1,N+1):
        w.append(map(int,e.readline().split()))
    C=0
    C2=0
    for j in xrange(0,len(w)-1):
        for h in range(j+1,len(w)):
            C+=compare(w[j],w[h])
            C2+=compare2(w[j],w[h])
    s.write('Case #%d: %d\n'%(i,min(C,C2)))
e.close()
s.close()
