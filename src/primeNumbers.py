def sumOfPrimes(n):
    if n <= 1:
        return 1
    prime = [True] * (n + 1) 
    p = 2
    while p * p < n+1:
        if prime[p] == True:
            i = p * 2  

            while i < n+1:
                prime[i] = False
                i += p
        p += 1
    tot = 0
    for i in range(2, n + 1):  
        if prime[i]:
            tot += i
    return tot
		