def is_prime_early_exit(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
print(f"{number} is prime: {is_prime_early_exit(number)}")
