def getSumOfMultiples(*numbers, _range):
    sum = 0
    for i in range(1, _range):
        already_multiple = False
        for number in numbers:
            if i % number == 0 and not already_multiple:
                already_multiple = True
                sum += i
    print(sum)

getSumOfMultiples(3, 5, _range=1000)