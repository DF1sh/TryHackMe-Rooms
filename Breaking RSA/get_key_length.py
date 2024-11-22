from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

# Percorso del file della chiave pubblica SSH
file_path = 'id_rsa.pub'

# Leggi il contenuto del file id_rsa.pub
with open(file_path, 'r') as file:
    key_str = file.read()

# Carica la chiave pubblica
key = load_ssh_public_key(key_str.encode(), backend=default_backend())

# Ottieni la lunghezza della chiave in bit
key_length = key.key_size

print(f"The length of the RSA key is: {key_length} bits")
