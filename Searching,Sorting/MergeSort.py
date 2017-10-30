def merge(A,l,m,r):
  # print A
  n1 = m-l+1
  n2 = r-m 
  
  L = [-1] * n1
  R = [-1] * n2
  
  for i in range(0 , n1):
    L[i] = A[l + i]

  for j in range(0 , n2):
    R[j] = A[m + 1 + j]
  
  i = j = 0
  k = l
  
  while i<n1 and j<n2:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
    k += 1
    
  while i < n1:
    A[k] = L[i]
    i += 1
    k += 1
    
  while j < n2:
    A[k] = R[j]
    j += 1
    k += 1
    
def MergeSort(A, l, r):
  
  if l < r:
    
    m = (l + r - 1)/2
    MergeSort(A,l,m)
    MergeSort(A,m+1,r)
    merge(A,l,m,r)
    
    
    
A = [10,1,8,6,4,7,9,2,3,5]
MergeSort(A,0,len(A)-1)
print A