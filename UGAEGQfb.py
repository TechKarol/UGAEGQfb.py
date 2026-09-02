import random
import string

print(r"""
 _   _  ____    _    _____ ____  ___   __ _
| | | |/ ___|  / \  | ____/ ___|/ _ \ / _| |__   _ __  _   _
| | | | |  _  / _ \ |  _|| |  _| | | | |_| '_ \ | '_ \| | | |
| |_| | |_| |/ ___ \| |__| |_| | |_| |  _| |_) || |_) | |_| |
 \___/ \____/_/   \_\_____\____|\__\_\_| |_.__(_) .__/ \__, |
                                                |_|    |___/
""")
print("1. Szyfruj\n2. Odszyfruj\n3. Wyjdź")

def szyfruj(tekst, klucz):
    return ''.join(chr((ord(c) - 65 + klucz) % 26 + 65) if c.isupper()
                   else chr((ord(c) - 97 + klucz) % 26 + 97) if c.islower()
                   else c for c in tekst)

def odszyfruj(tekst, klucz):
    return szyfruj(tekst, -klucz)

while True:
    wybor = input("wybierz opcje: ")

    if wybor == "1":
        tekst = input("Wpisz tekst do zaszyfrowania: ")
        klucz = random.randint(1, 25)
        wynik = szyfruj(tekst, klucz)
        print(f"Zaszyfrowano: {wynik}")
        print(f"Klucz: {klucz}")  # użytkownik musi zapamiętać/zapisać

    elif wybor == "2":
        tekst = input("Wpisz zaszyfrowany tekst: ")
        klucz = int(input("Podaj klucz: "))
        print(f"Odszyfrowano: {odszyfruj(tekst, klucz)}")

    elif wybor == "3":
        break   