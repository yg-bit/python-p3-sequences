def print_fibonacci(length):
    """Print a list containing the first `length` Fibonacci numbers."""
    fib = []
    if length <= 0:
        print(fib)
        return

    # seed the sequence
    fib.append(0)
    if length == 1:
        print(fib)
        return

    fib.append(1)

    # build the rest
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])

    print(fib)