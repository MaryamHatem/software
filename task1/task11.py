
def print_double_half_pyramid(height):
    if height < 1 or height > 8:
        print("Invalid height. Please enter a positive integer between 1 and 8.")
        return

    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end="")
        for j in range(i):
            print("#", end="")
        print("  ", end="")
        for j in range(i):
            print("#", end="")
        print()
while True:
        height = int(input("Enter the height of the double half-pyramid (1-8): "))
        print_double_half_pyramid(height)
