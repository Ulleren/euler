n = 2000000
primelist = n * [1]
primelist[0] = 0
primelist[1] = 0

i = 2
while i*i <= n:

    if primelist[i] == 0:
        i+=1
        continue

    else:
        for k in range(i*2, n, i):
            primelist[k] = 0
        i+=1

print("sieve færdig")
primesum = 0            
for m in range(0, n):
    if primelist[m] == 1:
        primesum += m

print(primesum)
