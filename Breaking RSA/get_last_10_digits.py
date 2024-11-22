from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

# Percorso del file della chiave pubblica SSH
file_path = 'id_rsa.pub'

# Leggi il contenuto del file id_rsa.pub
with open(file_path, 'r') as file:
    key_data = file.read()

# Carica la chiave pubblica
public_key = load_ssh_public_key(key_data.encode(), backend=default_backend())

# Accesso al modulo n (per chiavi RSA)
if hasattr(public_key, 'public_numbers'):
    n = public_key.public_numbers().n
    # Calcolo degli ultimi 10 cifre di n
    last_10_digits = n % (10**10)
    print("The last 10 digits of n are:", last_10_digits)
else:
    print("The provided key is not an RSA key.")
