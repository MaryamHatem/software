def sum(numbers, target):
    num_set = set()
    for num1 in numbers:
        num2 = target - num1
        if num2 in num_set:
            return num1, num2
        num_set.add(num1)
    return None

numbers = input("Enter a list of numbers: ").split()
numbers = [int(num1) for num1 in numbers]
x = int(input("Enter the number wanted: "))
pair = sum(numbers, x)

if pair is not None:
    print("Yes, {} = {} + {}".format(x, pair[0], pair[1]))
else:
    print("No")



