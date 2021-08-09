# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def getSumOfMultiples(*numbers, _range):
    sum = 0
    for i in range(1, _range):
        already_multiple = False
        for number in numbers:
            if i % number == 0 and not already_multiple:
                already_multiple = True
                sum += i
    print(sum)

def main():
    getSumOfMultiples(3, 5, _range=1000)

if __name__ == "__main__":
    main()