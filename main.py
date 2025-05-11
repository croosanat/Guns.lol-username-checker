import cloudscraper
from colorama import Fore, init

init(autoreset=True)
scraper = cloudscraper.create_scraper()

with open("username.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f if line.strip()]

for username in usernames:
    url = f"https://guns.lol/{username}"
    try:
        r = scraper.get(url, timeout=10)
        if r.status_code != 200:
            print(Fore.YELLOW + f"[!] Error {r.status_code} → {url}")
            continue

        if "This user is not claimed" in r.text:
            print(Fore.GREEN + f"[✓] Available: {username} → {url}")
        else:
            print(Fore.RED + f"[x] Taken: {username} → {url}")

    except Exception as e:
        print(Fore.YELLOW + f"[!] Failed to check {username}: {e}")
