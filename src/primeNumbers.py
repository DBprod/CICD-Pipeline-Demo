def sumOfPrimes(n):
    if n <= 1:
        return 1

    prime = [True] * (n + 1)  # list to store if number is prime numbers

    p = 2
    while p * p <= n:
        # if p is not changed in prime, then it is prime number
        if prime[p] == True:
            i = p * 2  # update all multiples of p

            while i <= n:
                prime[i] = False
                i += p
        p += 1

    totalSum = 0
    for i in range(2, n + 1):  # find the sum by looking into prime list
        if prime[i]:
            totalSum += i
    return totalSum
		
print(sumOfPrimes(30))