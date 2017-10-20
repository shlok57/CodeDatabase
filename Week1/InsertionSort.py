def InsertionSort(array):
  
  n = len(array)
  
  for i in range(n):
    
    temp = array[i]
    j = i
    
    while j>0 and temp < array[j-1]:
      array[j] = array[j-1]
      j = j-1
        
    array[j] = temp
      
  return array
  
  
A = [10,1,8,6,4,7,9,2,3,5]
A = InsertionSort(A)
print A