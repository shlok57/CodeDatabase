# Variables:
# N    : Int 		Length of Search Space
# M    : Int 		Search Key
# list : IntList 	Search Space 

# Returns:
# Index of (last ocuurence) search key, -1 if no results


N, M = map(int, raw_input().split())
list = map(int, raw_input().split())[::-1]

result = -1 

for i in range(N):
    if list[i] == M:
        result = N - i
        break

print result