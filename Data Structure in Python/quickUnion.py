id1=[]
def quickunion(n):
	for x in range(n):
		id1.append(x)
def find(p):
	while(p!=id1[p]):
		p=id1[p]
	return p
def connected(p,q):
	return find(p)==find(q)
def union(p,q):
	i = find(p)
	j = find(q)
	if(i ==j ):
		return
	id1[i]=j	
	print(id1)
n = int(input('enter number of input'))
i=1
quickunion(n)
while(i!=n):
	p = int(input('enter value of p'))
	q = int(input('enter value of q'))
	if(connected(p,q)==False):
		union(p,q)
		i +=1
	print(find(p))
