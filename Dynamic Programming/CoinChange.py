def CoinChange(d,p):
	n = len(d)
	for i in range(1,p+1):
		mini = 99999999
		for j in d:
			if j <= i and (1 + C[i-j]) < mini:
				mini = 1 + C[i-j];
				s = d.index(j)
		C[i] = mini
		S[i] = s

def print_Coins(c):
	while c > 0:
		print deno[S[c]], " ",
		c = c - deno[S[c]]


deno = [1, 3, 4]
p = 6
C = [0 for i in range(p+1)]
S = [0 for i in range(p+1)]
CoinChange(deno, p)
print "Denominations: ", str(deno)
print "Coin Change required: " + str(p)
print "#Coins: ", str(C[-1])
print "Coins: > ", 
print_Coins(p)