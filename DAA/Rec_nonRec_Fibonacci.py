
import time

# Non-Recursive (Iterative) Method
def fibonacci_non_recursive(n):
    a, b = 0, 1

    print("Fibonacci Series (Non-Recursive):")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Recursive Method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Main Program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")

else:
    # Non-Recursive Execution
    start = time.perf_counter()
    fibonacci_non_recursive(n)
    end = time.perf_counter()

    print("\nExecution Time:", end - start, "seconds")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")

    # Recursive Execution
    start = time.perf_counter()

    print("\n\nFibonacci Series (Recursive):")

    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    end = time.perf_counter()

    print("\nExecution Time:", end - start, "seconds")
    print("Time Complexity: O(2^n)")
    print("Space Complexity: O(n)")