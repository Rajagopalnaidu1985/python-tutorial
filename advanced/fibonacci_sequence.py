
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Example usage:
n = 10
print(f"Fibonacci number at position {n} is {fibonacci(n)}")








def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
n = 10
print(f"Fibonacci number at position {n} is {fibonacci(n)}")





def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Generate Fibonacci sequence up to the 20th number
n = 20
fib_sequence = fibonacci_sequence(n)

# Print the sequence
print(f"Fibonacci sequence up to the {n}th number:")
print(fib_sequence)




