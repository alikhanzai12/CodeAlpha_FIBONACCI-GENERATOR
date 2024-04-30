def fib_generator(n):
    fib_seq = [0,1]
    for i in range (2,n):
        fib_seq.append(fib_seq[-1]+fib_seq[-2])

    return fib_seq

n = 10
fib_result = fib_generator(n)
print(f"Fibonacci sequence up to {n} is {fib_result}")
