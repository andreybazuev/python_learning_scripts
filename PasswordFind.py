import random
import string

def password_find (password):
    length = len(password)
    characters = string.digits + string.ascii_letters 
    attempt = 0
    iterations = 0
    while password != str(attempt): #в строку, если attempt - число. Или рандом:
<<<<<<< HEAD
        attempt = ''.join(random.choice(characters) for i in range(length))
        #attempt += 1 #тупой перебор или рандом выше
=======
        #attempt = ''.join(random.choice(characters) for i in range(length))
        attempt += 1 #простой перебор. или рандом выше
>>>>>>> d6c2e8869567483d11af2032eebcf9c565ec42ec
        iterations += 1 
    return iterations

password = "4gc"
print ('iterations:', password_find(password))