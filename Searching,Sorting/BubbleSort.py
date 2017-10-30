def BubbleSort(array):
  
  n = len(array)
  
  for i in range(n-1):
    for j in range(n-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1],array[j]
        
  return array
  
A = [1,8,6,4,7,9,2,3,5]
A = BubbleSort(A)
print A