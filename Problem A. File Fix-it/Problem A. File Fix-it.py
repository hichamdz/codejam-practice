from node import Node
e=open("E:/entrer2.txt","r")
s=open("E:/sorter2.txt","w")
n=int(e.readline())
for i in range(1,n+1):
    N=e.readline().split()
    N,M=int(N[0]),int(N[1])
    tree=Node("root")
    for j in range(1,N+1):
        T=e.readline().replace('/',' ').split()
        f=tree
        for h in T:
            if h not in f.dfils:
               f.add_child(Node(h))
            k=f.dfils.index(h)
            f=f.fils[k]
        while f.pere!=None:f=f.pere
    C=0
    f=tree
    for j in range(1,M+1):
        T=e.readline().replace('/',' ').split()
        for h in T:
            if h not in f.dfils:
               f.add_child(Node(h))
               C+=1
            k=f.dfils.index(h)
            f=f.fils[k]
        while f.pere!=None:f=f.pere
    s.write('Case #%d: %d\n'%(i,C))
e.close()
s.close()
