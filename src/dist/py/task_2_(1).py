from collections import deque


def is_palindrome(s):
    """palindrome check"""
    normalize_s = "".join(c.lower() for c in s if c.isalnum())

    d = deque(normalize_s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


if __name__ == "__main__":
    s = input("Enter the string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
