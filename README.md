# E-Commerce
**Studente:** Andrea Sestito

**Matricola:** 7074084

## Tipo di Progetto
Full-Stack Web Application

## Framework
Django

## Descrizione
Piattaforma E-commerce Full-Stack sviluppata con Django. Il sistema gestisce l'intero flusso di vendita: dal catalogo prodotti e carrello dinamico, fino al checkout con aggiornamento automatico dello stock. Include un sistema di autenticazione che protegge le funzionalità di gestione del catalogo, riservate esclusivamente all'amministratore tramite pannello dedicato.

## Funzionalità Implementate
### Ruolo Cliente
- Registrazione e Login.
- Visualizzazione catalogo prodotti.
- Gestione carrello (aggiunta/rimozione prodotti).
- Checkout e aggiornamento disponibilità stock.

### Ruolo Amministratore
- Accesso riservato al pannello di controllo.
- Creazione/Modifica/Eliminazione prodotti e categorie.

## Istruzioni per l'esecuzione locale
1. Clona il repository: `git clone [https://github.com/andreasestito14-bk/Ecommerce_PPM2026.git]`
2. Crea un ambiente virtuale: `python -m venv venv`
3. Installa le dipendenze: `pip install -r requirements.txt`
4. Applica le migrazioni: `python manage.py migrate`
5. Avvia il server: `python manage.py runserver`

## Database
Il file `db.sqlite3` incluso contiene dati demo (categorie, prodotti, utenti) per testare immediatamente il progetto.

## Account Demo
- **Amministratore:**
  - Username: admin_demo
  - Password: admin12345
  - Ruolo: Admin
- **Cliente:**
  - Username: cliente1
  - Password: Test1234!
  - Ruolo: Cliente

## Link Deploy Online
https://ecommerce-ppm-andreas.onrender.com/

## Browser-based Testing Scenario
Di seguito un breve scenario di test per verificare il funzionamento dell'applicazione tramite browser:

### 1. Test Permessi e Creazione Dati (Ruolo Admin)
1. Clicca il link e vai alla homepage.
2. Clicca su **"Accedi"** ed effettua il login con l'account **Amministratore**.
3. Clicca sul link **"Pannello Admin"** nella navbar (che è visibile solo agli staff/admin).
4. Naviga nella sezione `Store > Products` e aggiungi un nuovo prodotto (es. "Cassa Bluetooth"), impostando una categoria, un prezzo e una disponibilità (stock) di 10 pezzi.
5. Torna al sito cliccando su "View site" in alto a destra.
6. Clicca su **"Esci (Logout)"**.

### 2. Navigazione e Controllo Permessi (Ruolo Cliente)
1. Clicca su **"Accedi"** ed effettua il login con l'account **`cliente1`**.
2. **Test Permessi:** Verifica che il link "Pannello Admin" *non* sia più visibile nella navbar.
3. Clicca su **"Catalogo Prodotti"** e verifica la presenza della nuova "Cassa Bluetooth" appena creata dall'admin.

### 3. Workflow di Acquisto e Verifica Risultati
1. Clicca su "Vedi Dettaglio" della "Cassa Bluetooth".
2. Clicca sul pulsante verde **"Aggiungi al Carrello"**.
3. Verrai reindirizzato al Carrello. Verifica che il Totale Parziale e il Totale Ordine siano calcolati correttamente.
4. Clicca sul pulsante nero **"Procedi al Pagamento Simulato"**.
5. **Verifica il risultato:** Atterrerai sulla pagina di successo ("Pagamento Ricevuto con Successo!"). 
6. Cliccando su "Torna al Catalogo", se torni nel dettaglio del "Cassa Bluetooth", vedrai che la disponibilità (stock) è diminuita di 1 unità, confermando l'aggiornamento del database post-checkout.