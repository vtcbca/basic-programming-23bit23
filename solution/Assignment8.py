def pattern_alphabets(n):
    width = (n * 2 - 1) * 4
    for i in range(n):
        row = [chr(65 + j) for j in range(i + 1)]
        row += row[-2::-1]  # Mirror the list
        print("   ".join(row).center(width))

# Example usage
pattern_alphabets(5)
