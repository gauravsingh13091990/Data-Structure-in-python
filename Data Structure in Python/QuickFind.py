id1 =[]
class unionfind():
	global count
	def unionFind(self,n):
		count =n
		for x in range(n):
			id1.append(x)
	def Count():
		return count
	def connected(self,p,q):
		return id1[p]==id1[q]
	def find(self,p):
		return id1[p]
	def union(self,p,q):
		pid = id1[p]
		qid = id1[q]
		if(pid == qid):
			return 
		for x in range(len(id1)):
			if(id1[x]==pid):
				id1[x]=qid
				# count-=1
		print(id1)
		# print(count)



n = int(input('Enter the number of input'))
i =1
ob = unionfind()
ob.unionFind(n)
while(i!=n):
	p = int(input('enter value of p'))
	q = int(input('enter value of q'))
	if(ob.connected(p,q) == False):
		ob.union(p,q)
		i+=1
	print(ob.find(p))
