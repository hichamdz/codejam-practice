import re
L,D,N=map(int,raw_input().split())
W=[]
for i in xrange(D):
	W.append(raw_input())
M=[]
for i in xrange(N):
	S=0
	t=re.compile(raw_input().replace('(','[').replace(')',']'))
	for j in W:
		if re.match(t,j)!=None and len(re.match(t,j).group())==L :S+=1
	print "Case #%d: %d"%(i+1,S)
