print("FIBONACCI SERIES USING RECURSION")

# Recursive function
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Main program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")

else:
    print("\nFibonacci Series:")

    for i in range(n):
        print(fibonacci(i), end=" ")

    print()