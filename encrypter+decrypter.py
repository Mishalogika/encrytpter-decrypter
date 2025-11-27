from cryptography.fernet import Fernet
import os

mode = input("Введите режим (e = encrypt, d = decrypt): ")
folder = input(r"Введите путь:")


if mode == "e":
    key = Fernet.generate_key()
    cipher = Fernet(key)
    for f in os.listdir(folder):
        p = os.path.join(folder, f)
        if os.path.isfile(p):
            with open(p, "rb") as file:
                data = file.read()
            enc = cipher.encrypt(data)
            with open(p, "wb") as file:
                file.write(enc)
    print("Готово. Ваш ключ:")
    print(key.decode())

elif mode == "d":
    key = input("Введите ключ: ").encode()
    cipher = Fernet(key)
    for f in os.listdir(folder):
        p = os.path.join(folder, f)
        if os.path.isfile(p):
            with open(p, "rb") as file:
                data = file.read()
            dec = cipher.decrypt(data)
            with open(p, "wb") as file:
                file.write(dec)
    print("Файлы расшифрованы.")
