def product(numbers):
    total = 0
    for item in range(len(numbers)):
        if item == 0:
            total = numbers[item]
        else:
            total *= numbers[item]
    return total

print product([])
