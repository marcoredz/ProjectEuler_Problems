# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    s = str(n)
    half = int(len(s) / 2)
    isOdd = True if len(s) % 2 == 0 else False
    if isOdd:
        s_take1 = s[:half]
        s_take2 = s[half:][::-1] #[::-1] to reverse
    else:
        s_take1 = s[:half]
        s_take2 = s[half+1:][::-1]
    return True if s_take1 == s_take2 else False 

n1 = 999
n2 = 999
i, j = n1, n2

prod = i * j
maxPal = prod
while i > 0:
    while j > 0:
        j -= 1
        prod = i * j
        if isPalindrome(prod):
            maxPal = prod
            break
    i -= 1

# else:
#     print(prod, "is the largest palindrome from product of ", fact1, " * ", fact2)
    
#999 999
#999 * 998 = 997002
#999 * 997 = 996003
#999 * 996 = 995004
#999 * 995 = 994005

#998 * 