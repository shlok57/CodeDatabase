def LCS(A,B):
	m = len(A) + 1
	n = len(B) + 1
	C = [[0 for i in range(m)] for j in range(n)]
	S = [[0 for i in range(m)] for j in range(n)]
	for i in range(1,m):
		for j in range(1,n):
			if A[i-1] == B[j-1]:
				C[i][j] = C[i-1][j-1] + 1
				S[i][j] = 'c'
			elif C[i-1][j] > C[i][j-1]:
				C[i][j] = C[i-1][j]
				S[i][j] = 'u'
			else:
				C[i][j] = C[i][j-1]
				S[i][j] = 'l'

	print "Longest Len: " + str(C[m-1][n-1])
	printSol(A,S,m-1,n-1)

def printSol(A,S,m,n):
	if m==0 or n == 0:
		return

	if S[m][n] == 'c':
		printSol(A,S,m-1,n-1)
		print A[m-1], " ", 
	elif S[m][n] == 'u':
		printSol(A,S,m-1,n)
	else:
		printSol(A,S,m,n-1)

def printList(L):
	for i in L:
		print str(i), ' ', 
	print

A = 'bcaabced'
B = 'cfabdccd'
print 'A: ',
printList(A)
print 'B: ',
printList(B)
LCS(A,B)