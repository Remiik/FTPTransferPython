import os
import time
import pysftp

def retry_connection(max_retries=10):
    for retry in range(max_retries):
        try:
            return
        except ConnectionError:
            print(f"Erreur de connexion. Tentative {retry+1} sur {max_retries}.")
            time.sleep(1)
    raise ConnectionError("Impossible de se connecter.")

print(f'\033[92m✔ Connection au serveur OK\033[0m')

while True:
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        srv = pysftp.Connection(host="arthurdanon.fr", username="serveur", password="Synology1*", cnopts=cnopts)
        srv.cwd('home')############ dossier sur le ftp ############
        filenames = srv.listdir()
        num_files = len(filenames)
        get_dir = '/Users/arthurdanon/Documents'############ chemin du depot #################
        for filename in filenames:
          local_get_file_path = os.path.join(get_dir, filename)
          srv.get(filename, local_get_file_path)
          srv.unlink(filename)
        srv.close()
        print(f'\033[92m{num_files} fichiers ont été envoyés\033[0m')
        break

    except Exception as e:
        print(f'\033[91mUne erreur est survenue: {e}\033[0m')
