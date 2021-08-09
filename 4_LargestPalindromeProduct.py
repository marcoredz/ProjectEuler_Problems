# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

def largestPalindromeProduct():
    n1 = 999
    n2 = 999
    i, j = n1, n2

    prod = i * j
    maxPal = prod
    maxArray = []
    while i > 0:
        j = i
        while j > 0:
            j -= 1
            prod = i * j
            if isPalindrome(prod):
                if prod > maxPal:
                    maxArray.append(prod)
                maxPal = prod
                break
        i -= 1

    print("Max", max(maxArray))

def main():
    largestPalindromeProduct()

if __name__ == "__main__":
    main()