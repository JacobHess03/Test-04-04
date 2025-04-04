# Inizializzazione del flag per controllare il ciclo principale e delle liste per memorizzare i dati
flag = True
numeri = []  # Lista per memorizzare i numeri
caratteri = []  # Lista per memorizzare i caratteri
booleani = []  # Lista per memorizzare i valori booleani

# Ciclo principale che continua fino a quando l'utente non decide di uscire
while flag:
    # Richiesta all'utente per scegliere un'azione
    scelta = input("Vuoi inserire un numero, un carattere o un booleano o stampare una lista? (n/c/b/s) oppure 'esci' per terminare: ").lower()
    
    # Gestione delle diverse opzioni scelte dall'utente
    match scelta:
        case 'n':  # Inserimento di un numero
            numero = float(input("Inserisci un numero: "))  # Conversione dell'input in float
            numeri.append(numero)  # Aggiunta del numero alla lista dei numeri
         
        case 'c':  # Inserimento di un carattere
            carattere = input("Inserisci un carattere: ")  # Richiesta di un carattere
            if len(carattere) == 1:  # Controllo che l'input sia un singolo carattere
                caratteri.append(carattere)  # Aggiunta del carattere alla lista dei caratteri
            else:
                print("Non è un carattere valido.")  # Messaggio di errore per input non valido
        
        case 'b':  # Inserimento di un valore booleano
            booleano = input("Inserisci un booleano (vero/falso): ").lower()  # Richiesta di un valore booleano
            if booleano in ['vero', 'falso']:  # Controllo che l'input sia valido
                booleani.append(booleano == 'vero')  # Conversione in booleano e aggiunta alla lista
            else:
                print("Non è un booleano valido.")  # Messaggio di errore per input non valido
        
        case 's':  # Stampa delle liste
            lista = input("Vuoi stampare la lista dei numeri, caratteri o booleani o tutte e tre? (n/c/b/t): ").lower()
            match lista:
                case 'n':  # Stampa della lista dei numeri
                    print("Lista numeri:", numeri)
                case 'c':  # Stampa della lista dei caratteri
                    print("Lista caratteri:", caratteri)
                case 'b':  # Stampa della lista dei booleani
                    print("Lista booleani:", booleani)
                case 't':  # Stampa di tutte le liste
                    print("Lista numeri:", numeri)
                    print("Lista caratteri:", caratteri)
                    print("Lista booleani:", booleani)
                case _:  # Gestione di input non valido
                    print("Scelta non valida.")
        
        case 'esci':  # Uscita dal programma
            flag = False  # Imposta il flag a False per terminare il ciclo
        
        case _:  # Gestione di input non valido
            print("Scelta non valida. Riprova.")