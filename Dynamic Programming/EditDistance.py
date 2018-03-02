def EditDistance(a,b):
	m = len(a) + 1
	n = len(b) + 1

	C = [[0 for i in range(n)] for j in range(m)]
	S = [['x' for i in range(n)] for j in range(m)]

	for i in range(1,m):
		C[i][0] = Cost['i'] + C[i-1][0]
		S[i][0] = 'i'

	for i in range(1,n):
		C[0][i] = Cost['d'] + C[0][i-1]
		S[0][i] = 'd'

	print_2dList(C)
	print_2dList(S)

	for i in range(1,m):
		for j in range(1,n):
			mini = 999999
			action = 'x'

			if i >= 1:
				if a[i-1] == b[j-1] and mini > C[i-1][j-1] + Cost['c']:
					mini = C[i-1][j-1] + Cost['c']
					action = 'c'
				if a[i-1] != b[j-1] and mini > C[i-1][j-1] + Cost['r']:
					mini = C[i-1][j-1] + Cost['r']
					action = 'r'
				if i < m and mini > C[i-1][j] + Cost['d']:
					mini = C[i-1][j] + Cost['d']
					action = 'd'
			if j >= 1:
				if j < n and mini > C[i][j-1] + Cost['i']:
					mini = C[i][j-1] + Cost['i']
					action = 'i'
			if i >= 2 and j >= 2:
				if i < m and j < n and a[i-1] == b[j-2] and a[i-2] == b[j-1] and mini > C[i-2][j-2] + Cost['t']:
					mini = C[i-2][j-2] + Cost['t']
					action = 't'

			C[i][j] = mini
			S[i][j] = action
			# print "Update:"
			# print_2dList(C)
			# print_2dList(S)	
			# print "End"
			
	print "Ans:"
	print_2dList(C)
	print_2dList(S)	
	print "Sol"
	print C[m-1][n-1]

def print_2dList(L):

	print "List: "
	for i in range(len(L)):
		for j in range(len(L[0])):
			print str(L[i][j]) + " ",
		print
	print "----\n"


# a = "algorithm"
# b = "altruistic"
a = raw_input("enter a: ")
b = raw_input("enter b: ")
Cost = {}
Cost['c'] = 3
Cost['r'] = 3
Cost['d'] = 2
Cost['i'] = 2
Cost['t'] = 1

EditDistance(a,b)
