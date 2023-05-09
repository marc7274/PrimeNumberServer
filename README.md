CONSEGNA
Si richiede di creare un sistema distribuito in grado di calcolare un numero primo e comunicare il risultato al server.

TECNOLOGIE UTILIZZATE
- Linguaggio python per la scrittura dei client e del server
- Json per la comunicazione di stringhe

VERSIONI 
Versione 0.0
1. client si avvia, apre la connessione e richiede il range di numeri al server
2. il server risponde 
3. il client chiude la connessione
4. successivamente il client calcola il range di numeri primi e riapre la connessione con il server
5. infine il client invia il risultato al server e chiude definitivamente la connessione

Versione 0.1
Per ottimizzare il programma non chiudiamo la connessione alla fine del loop per aprirla subito dopo come nella versione 0.0.
1. client si avvia, apre la connessione e richiede il range di numeri al server
2. il server risponde 
3. il client chiude la connessione
4. successivamente il client calcola il range di numeri primi
5. infine il client,  dopo aver riaperto la connessione ( nel primo punto ), invia il risultato al server e successivamente richiede un nuovo range

Versione 1.0
dizionario
- client_virus  = clienti che scarica il client_slave
- client_slave = client che calcola num primo


1. client_virus si aggiorna
2. client_virus si connette → manda al server un stringa con scritto che è una nuova connessione
3. server risponde con con il codice py del client_slave
4. client_virus scarica client_slave e lo runna  (virus chiude la connessione)
  a. slave chiede range di numeri al server
  b. il server risponde e chiude connessione
  c. lo slave calcola 
  d. manda i num al server
  e. chiude la connessione
  f. ricomincia 

