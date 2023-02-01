
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
time.sleep(0.5)
print("Support Server : https://discord.gg/F6AaxA3zwg")
time.sleep(0.3)
print("English Version")
time.sleep(0.2)

num = int(input('How many Nitro codes do you want to generate?: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("The nitro codes have been generated. Please wait a short while!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Duration: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Unvalid | {nitro} ")

input("\nYou have generated, now press enter to close this, you will get valid codes in Valid Codes.txt, if you see its empty then you are out of luck, generate 20 million codes for luck or else.")
