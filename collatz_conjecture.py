def collatz(number):
    count = 0
    if number > 1:
        while number > 1:
            if number % 2 == 0:
                number = number / 2
                count += 1
            else:
                number = (number*3)+1
                count += 1
    else:
        raise('You need to give a value higher than 1.')
    return count

