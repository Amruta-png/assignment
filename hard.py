def shortestPalindrome(s):
    # Function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    # Find the longest palindrome prefix
    i = len(s)
    while i > 0 and not is_palindrome(s[:i]):
        i -= 1

    # Add the reversed remaining suffix to the front
    return s[i:][::-1] + s

s = "aacecaaa"
result = shortestPalindrome(s)
print(result)  
a="abcd"
res=shortestPalindrome(a)
print(res)
