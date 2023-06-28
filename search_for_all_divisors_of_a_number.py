#поиск всех делителей числа
def find_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:           
            divisors.append(i)
    print (divisors)    
    return divisors

find_divisors(247)