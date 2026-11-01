import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr, low, high, count):

    if low < high:
        pivot_index = deterministic_partition(arr, low, high, count)

        deterministic_quick_sort(arr, low, pivot_index - 1, count)
        deterministic_quick_sort(arr, pivot_index + 1, high, count)


def deterministic_partition(arr, low, high, count):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        count[0] += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Randomized Quick Sort
def randomized_quick_sort(arr, low, high, count):

    if low < high:
        pivot_index = randomized_partition(arr, low, high, count)

        randomized_quick_sort(arr, low, pivot_index - 1, count)
        randomized_quick_sort(arr, pivot_index + 1, high, count)


def randomized_partition(arr, low, high, count):

    # Select a random pivot
    random_index = random.randint(low, high)

    # Move random pivot to the last position
    arr[random_index], arr[high] = arr[high], arr[random_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        count[0] += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Main Program
print("QUICK SORT ANALYSIS")
print("1. Deterministic Quick Sort")
print("2. Randomized Quick Sort")

n = int(input("\nEnter number of elements: "))

arr = []

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("\nOriginal Array:", arr)

# Deterministic Quick Sort
arr1 = arr.copy()
count1 = [0]

start = time.time()

deterministic_quick_sort(arr1, 0, n - 1, count1)

end = time.time()

time1 = end - start

print("\nDeterministic Quick Sort")
print("Sorted Array:", arr1)
print("Number of Comparisons:", count1[0])
print("Execution Time:", time1, "seconds")


# Randomized Quick Sort
arr2 = arr.copy()
count2 = [0]

start = time.time()

randomized_quick_sort(arr2, 0, n - 1, count2)

end = time.time()

time2 = end - start

print("\nRandomized Quick Sort")
print("Sorted Array:", arr2)
print("Number of Comparisons:", count2[0])
print("Execution Time:", time2, "seconds")


# Comparison
print("\nPERFORMANCE COMPARISON")

if count1[0] < count2[0]:
    print("Deterministic Quick Sort used fewer comparisons.")
elif count1[0] > count2[0]:
    print("Randomized Quick Sort used fewer comparisons.")
else:
    print("Both used the same number of comparisons.")