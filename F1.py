def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    fibs = [0] * (n + 1)
    fibs[0] = 0
    fibs[1] = 1

    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs


print(fibonacci(30))
