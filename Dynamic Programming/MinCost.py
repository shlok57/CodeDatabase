def Prof():
	C[0] = 0
	for i in range(1, N):
		mini = 99999
		# minnode =N
		for j in range(i):
			# print i,j
			print T[N-i-1]
			if mini > (C[j] + T[N-i-1][N-j-1]):
				mini = (C[j] + T[N-i-1][N-j-1])
				minnode = j
		print
		C[i] = mini
		S[i] = minnode
		
	print "Total Distance: " + str(C[N-1])
	print_path()
	# print S
	
def print_path():
	n = N-1
	while n > 0:
		print Names[N-n-1], " ",
		n = S[n]
	print Names[N-1]
		
T = [[0,5,10,12], [0,0,3,2], [0,0,0,4], [0,0,0,0]]
N = len(T)
Names = ['A', 'B', 'C', 'D']
C = [0 for i in range(N)]
S = [0 for i in range(N)]
Prof()