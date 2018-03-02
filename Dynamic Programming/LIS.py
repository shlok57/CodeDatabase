def LIS(A):
	n = len(A)
	C = [0 for i in range(n)]
	S = [-1 for i in range(n)]
	C[0] = 1
	for i in range(n):
		maxi = -99999
		sel = -1
		for j in range(i):
			if j < i and A[j] < A[i] and 1 + C[j] > maxi:
				maxi = 1 + C[j]
				sel = j
		if maxi == -99999:
			maxi = 1
		C[i] = maxi
		S[i] = sel

	print C
	print S
	print_Sol(A,S,n-1)

def print_Sol(A, S, n):
	if n != -1:
		print_Sol(A, S, S[n])
		print A[n],

A = [1,2,0,2,4,3,7]
LIS(A)