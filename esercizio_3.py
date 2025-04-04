# Creazione di un sistema per la gestione degli utenti con funzionalità di salvataggio, login e modifica dei dati.
# Il programma include un menù per interagire con le funzionalità e supporta più utenti.

utenti = []  # Lista per memorizzare gli utenti con email e password

# Funzione per salvare un nuovo utente
def salva_utente(email, password):
    for utente in utenti:  # Controllo se l'email è già presente
        if utente["email"] == email:
            print("Utente già esistente.")  # Messaggio di errore se l'utente esiste
            return False
    utenti.append({"email": email, "password": password})  # Aggiunta del nuovo utente alla lista
    return True  # Conferma del salvataggio

# Funzione per effettuare il login
def login(email, password):
    for utente in utenti:  # Iterazione sugli utenti per verificare le credenziali
        if utente["email"] == email and utente["password"] == password:
            return True  # Login riuscito
    return False  # Login fallito

# Funzione per modificare i dati di un utente
def modifica_utente(email, password):
    if login(email, password):  # Verifica delle credenziali tramite login
        print("Login effettuato.")  # Messaggio di conferma del login
        nuova_email = input("Inserisci nuova email: ")  # Richiesta della nuova email
        nuova_password = input("Inserisci nuova password: ")  # Richiesta della nuova password
        for utente in utenti:  # Iterazione sugli utenti per trovare quello da modificare
            if utente["email"] == email and utente["password"] == password:
                utente["email"] = nuova_email  # Aggiornamento dell'email
                utente["password"] = nuova_password  # Aggiornamento della password
                return True  # Modifica riuscita
    else:  
        print("Email o password errati.")  # Messaggio di errore se le credenziali sono errate
        return False  # Modifica fallita
   
    return False  # Caso di fallback, modifica fallita

flag = True  # Flag per controllare il ciclo principale
while flag:
    # Menù principale per scegliere un'azione
    print("1. Salva utente")  # Opzione per salvare un nuovo utente
    print("2. Login")  # Opzione per effettuare il login
    print("3. Modifica utente")  # Opzione per modificare i dati di un utente
    print("4. Esci")  # Opzione per uscire dal programma
    scelta = input("Scegli un'opzione: ")  # Richiesta della scelta all'utente
    
    match scelta:
        case '1':  # Caso per salvare un nuovo utente
            email = input("Inserisci email: ")  # Richiesta dell'email
            password = input("Inserisci password: ")  # Richiesta della password
            if salva_utente(email, password):  # Chiamata alla funzione di salvataggio
                print("Utente salvato.")  # Messaggio di conferma
            else:
                print("Errore nel salvataggio dell'utente.")  # Messaggio di errore
        case '2':  # Caso per effettuare il login
            email = input("Inserisci email: ")  # Richiesta dell'email
            password = input("Inserisci password: ")  # Richiesta della password
            if login(email, password):  # Chiamata alla funzione di login
                print("Login effettuato.")  # Messaggio di conferma
            else:
                print("Email o password errati.")  # Messaggio di errore
        case '3':  # Caso per modificare i dati di un utente
            email = input("Inserisci email: ")  # Richiesta dell'email
            password = input("Inserisci password: ")  # Richiesta della password
            if modifica_utente(email, password):  # Chiamata alla funzione di modifica
                print("Utente modificato.")  # Messaggio di conferma
            else:
                print("Errore nella modifica dell'utente.")  # Messaggio di errore
        case '4':  # Caso per uscire dal programma
            flag = False  # Imposta il flag a False per terminare il ciclo
        case _:  # Caso per input non valido
            print("Scelta non valida.")  # Messaggio di errore per scelta non valida