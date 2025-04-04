# Creazione di un sistema che gestisce la lunghezza delle stringhe inserite
# L'utente può continuare a inserire stringhe finché la nuova stringa è più lunga della precedente
# Alla fine, il programma stampa le stringhe inserite separate da virgole e il numero totale di stringhe

flag = True  # Flag per controllare il ciclo
lunghezza = 0  # Variabile per memorizzare la lunghezza della stringa precedente
stringhe = []  # Lista per memorizzare le stringhe inserite

# Ciclo principale per l'inserimento delle stringhe
while flag:
    stringa = input("Inserisci una stringa: ")  # Richiesta di una stringa all'utente
    if len(stringa) > lunghezza:  # Controllo se la lunghezza della stringa è maggiore della precedente
        lunghezza = len(stringa)  # Aggiornamento della lunghezza massima
        stringhe.append(stringa)  # Aggiunta della stringa alla lista
    else:
        flag = False  # Interruzione del ciclo se la stringa è più corta o uguale

# Stampa delle stringhe inserite separate da virgole
print("Stringhe inserite: ", end='')  # Messaggio iniziale senza andare a capo
for stringa in stringhe:  # Iterazione sulle stringhe nella lista
    if stringa != stringhe[-1]:  # Controllo se la stringa non è l'ultima della lista
        print(stringa, end=', ')  # Stampa della stringa seguita da una virgola
    else:
        print(stringa)  # Stampa dell'ultima stringa senza virgola

