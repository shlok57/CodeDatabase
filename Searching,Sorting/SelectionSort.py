def SelectionSort(array):
  
  n = len(array)
  
  for i in range(n):
    min_index = i
    for j in range(i+1,n):
      if array[min_index] > array[j]:
        min_index = j
    
    array[i], array[min_index] = array[min_index],array[i]
    print array    
  return array
  
A = [10,1,8,6,4,7,9,2,3,5]
A = SelectionSort(A)
print A