# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,

def main():
    n_terms = 4000000
    n1, n2 = 0, 1
    fib, sum = 0, 0
    while fib < n_terms:
        fib = n1 + n2
        n1 = n2
        n2 = fib
        if fib % 2 == 0:
            sum += fib

    print(sum)

if __name__ == "__main__":
    main()