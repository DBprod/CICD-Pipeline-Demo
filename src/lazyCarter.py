def lazyCarterSum(n):
    sum = 0
    i = 1
    while i <= n:
        sum += (i * (i + 1)) // 2 + 1
        i += 1
    return int(sum)
