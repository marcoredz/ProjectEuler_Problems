# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def main():
    n = 600851475143
    div = 2
    maxFact = 0
    while (n != 0):
        if (n % div != 0):
            div += 1
        else:
            maxFact = n
            n /= div
            if (n == 1):
                print("The largest prime factor is: ", maxFact)
                break

if __name__ == "__main__":
    main()



