#используем срез строки выводя в ее обратном порядке [::-1] и сравнивая с оригиналом
def is_palindrome(word):
    
    if (word[:]) == (word[::-1]):
        print ('this is a palindrome') 
    else:
        print ("it's not a palindrome")

is_palindrome('утоп в поту')
