print("BINOMIAL COEFFICIENTS USING DYNAMIC PROGRAMMING")

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

if k < 0 or k > n:
    print("Invalid input! k must be between 0 and n.")

else:
    # Create a DP table
    dp = [[0 for j in range(k + 1)] for i in range(n + 1)]

    print("\nCalculating Binomial Coefficients...")

    for i in range(n + 1):
        for j in range(min(i, k) + 1):

            # Base conditions
            if j == 0 or j == i:
                dp[i][j] = 1

            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

            print("C(", i, ",", j, ") =", dp[i][j])

    print("\nBinomial Coefficient C(", n, ",", k, ") =", dp[n][k])