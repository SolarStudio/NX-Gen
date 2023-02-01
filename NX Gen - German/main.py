
import requests
import random
import string
import time

print("""
 ▄▄        ▄  ▄       ▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
▐░░▌      ▐░▌▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
▐░▌░▌     ▐░▌ ▐░▌   ▐░▌      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌
▐░▌▐░▌    ▐░▌  ▐░▌ ▐░▌       ▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌
▐░▌ ▐░▌   ▐░▌   ▐░▐░▌        ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌
▐░▌  ▐░▌  ▐░▌    ▐░▌         ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌
▐░▌   ▐░▌ ▐░▌   ▐░▌░▌        ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌
▐░▌    ▐░▌▐░▌  ▐░▌ ▐░▌       ▐░▌       ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌
▐░▌     ▐░▐░▌ ▐░▌   ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌
▐░▌      ▐░░▌▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌
 ▀        ▀▀  ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ """)
time.sleep(2)
print("Discord Nitro Generator")
time.sleep(0.3)
print("German Version / Deutsche Version")
time.sleep(0.2)

num = int(input('Wie viele Nitro Codes möchtest du generieren: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Die Nitro Codes wurden generiert. Bitte warte eine kurze Weile!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generiert {num} codes | Dauer: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Gültig | {nitro} ")
            break
        else:
            print(f" Ungültig | {nitro} ")

input("\nSie haben generiert, Jetzt drücken Sie die Eingabetaste, um diese zu schließen, erhalten Sie gültige Codes in Valid Codes.txt, wenn Sie sehen, seine leer dann sind Sie Pech, generieren 20 Millionen Codes für Glück oder sonst.")
