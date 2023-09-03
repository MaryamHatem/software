def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = input("enter numbers in order with spaces in between: ").split()
arr = [int(num) for num in arr]
target = int(input("Enter the wanted number: "))

result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
