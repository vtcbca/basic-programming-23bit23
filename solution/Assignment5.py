def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
print(is_palindrome("level"))  # True
print(is_palindrome("python"))  # False
