def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = input("Enter the numbers with spaces in between: ").split()
arr = [int(num) for num in arr]
bubble_sort(arr)
print("Sorted array:", arr)
