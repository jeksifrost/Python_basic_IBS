def new_filter(num):
    if num > 50 and num % 2 == 0:
        return True
    else:
        return False
    
numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

new_nums = filter(new_filter, numbers)

print(list(new_nums))