'''
generate subsets and sort alphabetically
'''

def give_subset(string):
  subsets = []
  actual = []
  helper(string, subsets, 0, actual)
  return actual
  
def helper(string, subsets, i, actual):
  # print subsets, " ", i
  if i == len(string):
    actual.append(subsets)
  else:
    helper(string, subsets, i+1, actual)
    helper(string, subsets + [string[i]], i+1, actual)
    
r = give_subset("abc")
print sorted(r, key=lambda x: (len(x),x))