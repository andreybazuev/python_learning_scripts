
def is_palindrome(word):
    l = int(len(word) / 2)   
    for i in range(0, l):
        s1 = word[0]
        s2 = word[-1]
        if word[0] == word[-1]:
            word = word[1:-1]
            #is_palindrome(word[1:-1])
        else:
            return("it's not a palindrome")
    return('this is a palindrome')      

print(is_palindrome('утоп в поту'))
