import random
import string

def generate_password(length):
    """Генерирует пароль заданной длины"""
    # Создаем строку, содержащую все символы, которые могут быть использованы в пароле
    characters = string.ascii_letters + string.digits
    # Генерируем пароль из случайных символов
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Пример использования
password = generate_password(15)
print(password)
