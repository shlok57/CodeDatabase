def LCS(A,B):
  m = len(A) + 1
  n = len(B) + 1
  C = [[0 for i in range(n)] for j in range(m)]
  S = [[0 for i in range(n)] for j in range(m)]
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

  # print A, " <> " , B, " <> ", str(C[m-1][n-1])
  return C[m-1][n-1], S

def getSol(A,S,m,n):
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

def PLCS(A):
  m = len(A)
  n = -999999
  D = []
  for i in range(1,m-1):
    # printList(A[:i])
    # printList(A[i:])
    temp = LCS(A[:i], A[:i-1:-1])
    # print temp[0]
    if n < temp[0] * 2:
      # print "here"
      n = temp[0] * 2
      D = temp[1]
    temp = LCS(A[:i],A[:i:-1])
    if n < temp[0] * 2 + 1:
      n = temp[0] * 2 + 1
      D = temp[1]

  print "Longest Palindrome CS " + str(n)

A = 'bcbaabced'
B = 'cfabdccdy'
print 'A: ',
printList(A)
print 'B: ',
printList(B)
PLCS(A)