def quicksort(A, l, r):
	if l < r:

		splitpoint = partition(A,l,r)

		quicksort(A,l,splitpoint-1)
		quicksort(A,splitpoint+1,r)

def partition(A, l, r):
	pivot = A[l]

	left = l+1
	right = r

	crossed = False
	while not crossed:
		while left <= right and A[left] <= pivot:
			left += 1
		while left <= right and A[right] >= pivot:
			right -= 1

		if right < left:
			crossed = True
		else:
			A[left], A[right] = A[right], A[left]

	A[right], A[l] = A[l], A[right]
	return right


A = [4,7,1,9,8,2,5,0,6,3]
quicksort(A, 0, len(A) - 1)
print A