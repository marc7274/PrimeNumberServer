DOCUMENTAZIONE
Consegna
Si richiede di creare un sistema distribuito in grado di calcolare un numero primo e comunicare il risultato al server.

Tecnologie utilizzate
Linguaggio python per la scrittura dei client e del server
Json per la comunicazione di stringhe

Progettazione versioni
Versione 0.0
client si avvia, apre la connessione e richiede il range di numeri al server
il server risponde 
il client chiude la connessione
successivamente il client calcola il range di numeri primi e riapre la connessione con il server
infine il client invia il risultato al server e chiude definitivamente la connessione
Schema di funzionamento

Versione 0.1
Per ottimizzare il programma non chiudiamo la connessione alla fine del loop per riaprila subito dopo come nella versione 0.0.
client si avvia, apre la connessione e richiede il range di numeri al server
il server risponde 
il client chiude la connessione
successivamente il client calcola il range di numeri primi
infine il client,  dopo aver riaperto la connessione ( nel primo punto ), invia il risultato al server e successivamente richiede un nuovo range
Versione 1.0

Versione 2.0
dizionario
cli
client_virus  = clienti che scarica il client_slave
client_slave = client che calcola num primo


client_virus si aggiorna
client_virus si connette → manda al server un stringa con scritto che è una nuova connessione
server risponde con con il codice py del client_slave
client_virus scarica client_slave e lo runna  (virus chiude la connessione)
slave chiede range di numeri al server
il server risponde e chiude connessione
lo slave calcola 
manda i num al server
chiude la connessione
//client_slave si aggiorna ( in un secondo momento)
ricomincia 
Schema di funzionamento


