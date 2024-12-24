def print_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print(" ".join(str(j) for j in range(1, 2 * i)))

# Call the function
n = int(input("Enter the number of lines: "))
print_triangle(n)
