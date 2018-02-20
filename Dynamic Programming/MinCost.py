def Prof():
	C[0] = 0
	for i in range(1, N):
		mini = 99999
		for j in range(i):
			if mini > (C[j] + T[i][j]):
				mini = (C[j] + T[i][j])
				minnode = j
		C[i] = mini
		S[i] = minnode
		
	# print C
	print "Total Distance: " + str(C[N-1])
	print_path()
	# print S
	
def print_path():
	n = N-1
	while n > 0:
		print Names[N-n-1], " ",
		n = S[n]
	print Names[N-1]
		
T = [[0,0,0,0] , [4,0,0,0] , [6,3,0,0] , [12,10,5,0]]
N = len(T)
Names = ['A', 'B', 'C', 'D']
C = [0 for i in range(N)]
S = [0 for i in range(N)]
Prof()