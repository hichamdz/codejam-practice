def solve(_,C,n,itmes):
	for i in xrange(n):
		for j in xrange(i+1,n):
			if itmes[i]+itmes[j]==C:
				return "Case #%d: %d %d"%(_+1,i+1,j+1)
for t in xrange(input()):
	print(solve(t,input(),input(),map(int,raw_input().split())))
	
