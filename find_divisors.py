#поиск делителей заданного числа
def find_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

print(find_divisors(21))
