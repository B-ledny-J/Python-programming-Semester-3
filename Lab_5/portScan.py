import socket
import sys
from datetime import datetime

# Перевіряємо, чи були надані необхідні аргументи
if len(sys.argv) != 4:
    print("Використання: python scanner.py <хост> <початковий_порт> <кінцевий_порт>")
    sys.exit()

# Призначаємо аргументи змінним
target_host = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

# Список кортежів з поширеними сервісами
services = [
    (21, 'FTP'),
    (22, 'SSH'),
    (23, 'Telnet'),
    (25, 'SMTP'),
    (53, 'DNS'),
    (80, 'HTTP'),
    (110, 'POP3'),
    (143, 'IMAP'),
    (443, 'HTTPS')
]

try:
    # Отримуємо IP-адресу з доменного імені, якщо це необхідно
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print(f"Помилка: Не вдалося розпізнати хост '{target_host}'")
    sys.exit()

# Виводимо інформацію про початок сканування
print("-" * 50)
print(f"Сканування хоста: {target_ip}")
print(f"Час початку: {datetime.now()}")
print("-" * 50)

open_ports = []

try:
    # Головний цикл для перевірки кожного порту
    for port in range(start_port, end_port + 1):
        # Створюємо новий об'єкт сокета для кожного порту
        # AF_INET означає, що ми використовуємо IPv4
        # SOCK_STREAM означає, що це TCP-сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Встановлюємо таймаут для спроби з'єднання (в секундах)
        # Це важливо, щоб скрипт не "зависав" надовго
        sock.settimeout(1)

        # Намагаємося підключитися до хоста на вказаний порт
        # .connect_ex() повертає 0, якщо з'єднання успішне (порт відкритий)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service_name = "Невідомий сервіс"

            # Пошук сервісу через цикл по списку кортежів
            for service_port, service in services:
                if port == service_port:
                    service_name = service
                    break

            print(f"Порт {port}: \t Відкритий ({service_name})")
            open_ports.append((port, service_name))

        # Закриваємо сокет після кожної спроби
        sock.close()
except KeyboardInterrupt:
    print("\nСканування перервано користувачем.")
    sys.exit()
except socket.error:
    print("Помилка: Не вдалося з'єднатися з сервером.")
    sys.exit()

# Виводимо результати
print("-" * 50)
if open_ports:
    print("Сканування завершено.")
    print(f"Знайдено відкриті порти: {open_ports}")
else:
    print("Відкритих портів у вказаному діапазоні не знайдено.")
print("-" * 50)
