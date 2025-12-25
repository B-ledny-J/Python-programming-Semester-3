import hashlib
import os

def secure_store(password):
    # 1. Генерація солі (16 байт випадкових даних)
    salt = os.urandom(16).hex()

    # 2. Об'єднання
    salted_password = salt + password

    # 3. Хешування (SHA-256)
    hash_obj = hashlib.sha256(salted_password.encode('utf-8'))
    hashed_pass = hash_obj.hexdigest()

    # 4. Результат
    return f"{salt}${hashed_pass}"

new_pass = "Admin@123"
print(f"Збережено в БД: {secure_store(new_pass)}")