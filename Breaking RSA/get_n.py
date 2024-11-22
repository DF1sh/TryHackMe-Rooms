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
    print("N is:", n)
else:
    print("The provided key is not an RSA key.")
