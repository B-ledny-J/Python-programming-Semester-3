import hashlib

def crack_hash(target_hash, algorithm):
    print(f"Пошук пароля для хешу: {target_hash} ({algorithm})")

    for password in range(100000000, 1000000000):
        # Кодування рядка в байти
        password_str = f"{password:09d}"
        encoded_pass = password_str.encode('utf-8')

        # Хешування
        if algorithm == 'MD5':
            digest = hashlib.md5(encoded_pass).hexdigest()
        elif algorithm == 'SHA-1':
            digest = hashlib.sha1(encoded_pass).hexdigest()
        elif algorithm == 'SHA-256':
            digest = hashlib.sha256(encoded_pass).hexdigest()

        # Перевірка
        if digest == target_hash:
            print(f"[УСПІХ] Пароль знайдено: {password}")
            return password

    print("[НЕВДАЧА] Пароль не знайдено у словнику.")
    return None

target = "f7c3bc1d808e04732adf679965ccc34ca7ae3441"
crack_hash(target, "SHA-1")