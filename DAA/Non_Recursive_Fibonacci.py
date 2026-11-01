print("FIBONACCI SERIES USING ITERATION")

# Main program
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")

else:
    a = 0
    b = 1

    print("\nFibonacci Series:")

    for i in range(n):

        print(a, end=" ")

        # Calculate next Fibonacci number
        c = a + b

        a = b
        b = c

    print()