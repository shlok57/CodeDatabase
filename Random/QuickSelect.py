def Random_Partition (A,p,r):
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i = i + 1
			A[j] , A[i] = A[i], A[j]
	A[i+1], A[r] = A[r] , A[i+1]	
	return i + 1

def QuickSelect(A,p,r,i):
	if p == r:
		return A[p]
	q = Random_Partition(A,p,r)
	k = q-p+1
	if i == k:
		return A[q]
	elif i<k:
		return QuickSelect(A,p,q-1,i)
	else:
		return QuickSelect(A,q+1,r,i-k)


A = [1,5,2,8,7,6,9,3]
print QuickSelect(A,0,len(A)-1,1)
print A