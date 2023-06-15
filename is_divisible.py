def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

if is_divisible(6, 0) == True:
    print("x делится на y")
else:
    print("x не делится на y")