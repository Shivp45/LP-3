# Fractional Knapsack using Greedy Method

def fractional_knapsack(weights, profits, capacity):

    n = len(weights)
    items = []

    print("\n----- PROFIT / WEIGHT RATIO CALCULATION -----")

    # Calculate profit/weight ratio
    for i in range(n):

        ratio = profits[i] / weights[i]

        print("Item", i + 1)
        print("Profit:", profits[i])
        print("Weight:", weights[i])
        print("Ratio =", profits[i], "/", weights[i], "=", round(ratio, 2))
        print()

        items.append((ratio, weights[i], profits[i], i + 1))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    print("\n----- ITEMS SORTED BY RATIO -----")

    for ratio, weight, profit, item_no in items:
        print("Item", item_no,
              "| Weight:", weight,
              "| Profit:", profit,
              "| Ratio:", round(ratio, 2))

    total_profit = 0

    print("\n----- ITEM SELECTION PROCESS -----")

    # Select items according to maximum ratio
    for ratio, weight, profit, item_no in items:

        if capacity == 0:
            break

        if weight <= capacity:

            # Take complete item
            capacity -= weight
            total_profit += profit

            print("\nChoosing Item", item_no)
            print("Reason: Complete item fits in remaining capacity.")
            print("Taking 100% of Item", item_no)
            print("Profit Added:", profit)
            print("Remaining Capacity:", capacity)

        else:

            # Take fractional item
            fraction = capacity / weight

            added_profit = profit * fraction

            print("\nChoosing Item", item_no)
            print("Reason: Complete item does not fit.")
            print("Taking Fraction:", round(fraction, 2))
            print("Percentage Taken:", round(fraction * 100, 2), "%")
            print("Profit Added:", round(added_profit, 2))

            total_profit += added_profit
            capacity = 0

    print("\n----- FINAL RESULT -----")
    print("Maximum Profit:", round(total_profit, 2))


# Main Program
print("FRACTIONAL KNAPSACK PROBLEM")
print("--------------------------------")

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):

    print("\nEnter details of Item", i + 1)

    weight = float(input("Enter weight: "))
    profit = float(input("Enter profit: "))

    weights.append(weight)
    profits.append(profit)

capacity = float(input("\nEnter knapsack capacity: "))

fractional_knapsack(weights, profits, capacity)