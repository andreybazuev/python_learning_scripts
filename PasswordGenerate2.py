"""Генерирует пароль заданной длины"""
import secrets
import string

def generate_password(length):
    
    # Создаем строку, содержащую все символы, которые могут быть использованы в пароле
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерируем пароль из случайных символов
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# Пример использования
password = generate_password(15)
print(password)
