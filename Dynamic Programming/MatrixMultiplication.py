def MatMul(p):
  n = len(p)
  m = [[0 for i in range(n)] for j in range(n)]
  s = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    m[i][i] = 0
  
  for l in range(2,n):
    for i in range(1,n-l+1):
      j = i+l-1
      m[i][j] = 9999999
      for k in range(i, j):
        q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p [j]
        if q < m[i][j]:
          m[i][j] = q
          s[i][j] = k
  
  for i in m:
    for j in i:
      print str(j) + "\t",
    print
  
  print 
  print_sol(s,1,n-1)
  
  return m[1][n-1]
  
def print_sol(s,i,j):
	if i == j:
		print 'A'+str(i),
	else:
		print "(",
		print_sol(s,i,s[i][j])
		print_sol(s,s[i][j]+1,j)
		print ")",
		
		
p = [5,10,3,12,5,50,6]
print "\nSolution: " + str(MatMul(p))