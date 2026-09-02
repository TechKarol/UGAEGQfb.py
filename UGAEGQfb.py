import random


def wybierz_jezyk():
    print("Select language / Wybierz język:")
    print("1. Polski")
    print("2. English")

    while True:
        wybor = input("Choose / Wybierz: ")

        if wybor == "1":
            return "pl"
        elif wybor == "2":
            return "en"
        else:
            print("Invalid option / Nieprawidłowa opcja.")


jezyk = wybierz_jezyk()


teksty = {
    "pl": {
        "encrypt": "Szyfruj",
        "decrypt": "Odszyfruj",
        "exit": "Wyjdź",
        "choose": "Wybierz opcję: ",
        "encrypt_text": "Wpisz tekst do zaszyfrowania: ",
        "encrypted": "Zaszyfrowano",
        "key": "Klucz",
        "decrypt_text": "Wpisz zaszyfrowany tekst: ",
        "enter_key": "Podaj klucz: ",
        "decrypted": "Odszyfrowano",
        "invalid": "Nieprawidłowa opcja."
    },

    "en": {
        "encrypt": "Encrypt",
        "decrypt": "Decrypt",
        "exit": "Exit",
        "choose": "Choose option: ",
        "encrypt_text": "Enter text to encrypt: ",
        "encrypted": "Encrypted",
        "key": "Key",
        "decrypt_text": "Enter encrypted text: ",
        "enter_key": "Enter key: ",
        "decrypted": "Decrypted",
        "invalid": "Invalid option."
    }
}


print(r"""
 _   _  ____    _    _____ ____  ___   __ _
| | | |/ ___|  / \  | ____/ ___|/ _ \ / _| |__   _ __  _   _
| | | | |  _  / _ \ |  _|| |  _| | | | |_| '_ \ | '_ \| | | |
| |_| | |_| |/ ___ \| |__| |_| | |_| |  _| |_) || |_) | |_| |
 \___/ \____/_/   \_\_____\____|\__\_\_| |_.__(_) .__/ \__, |
                                                |_|    |___/
""")


def szyfruj(tekst, klucz):
    return ''.join(
        chr((ord(c) - 65 + klucz) % 26 + 65)
        if c.isupper()
        else chr((ord(c) - 97 + klucz) % 26 + 97)
        if c.islower()
        else c
        for c in tekst
    )


def odszyfruj(tekst, klucz):
    return szyfruj(tekst, -klucz)


while True:

    print()
    print("1.", teksty[jezyk]["encrypt"])
    print("2.", teksty[jezyk]["decrypt"])
    print("3.", teksty[jezyk]["exit"])

    wybor = input(teksty[jezyk]["choose"])

    if wybor == "1":

        tekst = input(teksty[jezyk]["encrypt_text"])

        klucz = random.randint(1, 25)

        wynik = szyfruj(tekst, klucz)

        print(f"{teksty[jezyk]['encrypted']}: {wynik}")
        print(f"{teksty[jezyk]['key']}: {klucz}")

    elif wybor == "2":

        tekst = input(teksty[jezyk]["decrypt_text"])

        klucz = int(input(teksty[jezyk]["enter_key"]))

        wynik = odszyfruj(tekst, klucz)

        print(f"{teksty[jezyk]['decrypted']}: {wynik}")

    elif wybor == "3":

        break

    else:

        print(teksty[jezyk]["invalid"])
