# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, profits, capacity):

    n = len(weights)

    # Display item details
    print("\n----- ITEM DETAILS -----")

    for i in range(n):
        print("Item", i + 1,
              "| Weight:", weights[i],
              "| Profit:", profits[i])

    # Create DP table
    dp = [[0 for j in range(capacity + 1)]
          for i in range(n + 1)]

    print("\n----- DYNAMIC PROGRAMMING EXECUTION -----")

    # Fill DP table
    for i in range(1, n + 1):

        print("\nConsidering Item", i)
        print("Weight:", weights[i - 1])
        print("Profit:", profits[i - 1])

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                print("\nCapacity:", w)
                print("Include Item Profit:", include)
                print("Exclude Item Profit:", exclude)

                dp[i][w] = max(include, exclude)

                if include > exclude:
                    print("Decision: Include Item", i)

                elif exclude > include:
                    print("Decision: Exclude Item", i)

                else:
                    print("Decision: Both choices give equal profit")

                print("Maximum Profit:", dp[i][w])

            else:

                dp[i][w] = dp[i - 1][w]

                print("\nCapacity:", w)
                print("Item cannot fit. Exclude Item", i)
                print("Maximum Profit:", dp[i][w])

    # Display DP table
    print("\n----- FINAL DP TABLE -----")

    for row in dp:
        print(row)

    # Find maximum profit
    max_profit = dp[n][capacity]

    print("\nMaximum Profit:", max_profit)

    # Trace back to find selected items
    print("\n----- SELECTED ITEMS -----")

    w = capacity
    selected = []

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(i)

            print("Item", i, "Selected")
            print("Weight:", weights[i - 1])
            print("Profit:", profits[i - 1])

            w -= weights[i - 1]

        else:
            print("Item", i, "Not Selected")

    selected.reverse()

    total_weight = sum(weights[i - 1] for i in selected)

    print("\n----- FINAL RESULT -----")
    print("Selected Items:", selected)
    print("Total Weight:", total_weight)
    print("Maximum Profit:", max_profit)
    print("Remaining Capacity:", capacity - total_weight)


# Main Program
print("0/1 KNAPSACK USING DYNAMIC PROGRAMMING")
print("----------------------------------------")

n = int(input("Enter the number of items: "))

weights = []
profits = []

for i in range(n):

    print("\nEnter details of Item", i + 1)

    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = int(input("\nEnter knapsack capacity: "))

knapsack(weights, profits, capacity)