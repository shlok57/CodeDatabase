def binary_search(A, low, high, key):
  while low <= high :
    
    mid = (low + high) / 2
    # print mid
    if A[mid] > key:
      high = mid - 1
    elif A[mid] < key:
      low = mid + 1
    else:
      return mid
  else:
    return -1

A = map(int, raw_input("Enter Sorted Array: ").split())
K = int(raw_input("Enter Search Key: "))

print binary_search(A,0,len(A)-1,K)