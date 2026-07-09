# E-Commerce PPM

Progetto di esame. Applicazione Full-Stack sviluppata con Django.

Sono disponibili i seguenti account demo:

- **Amministratore (Admin)**
  - Username: `admin_demo`
  - Password: `admin12345`
  - *Ruolo: Accesso al backend, gestione prodotti e categorie.*

- **Cliente (Customer)**
  - Username: `cliente1`
  - Password: `Test1234!`
  - *Ruolo: Navigazione catalogo, gestione carrello e checkout.*

---

## Browser-based Testing Scenario
Di seguito un breve scenario di test per verificare il funzionamento dell'applicazione tramite browser:

### 1. Test Permessi e Creazione Dati (Ruolo Admin)
1. Avvia il server e vai alla homepage.
2. Clicca su **"Accedi"** ed effettua il login con l'account **Amministratore**.
3. Clicca sul link **"Pannello Admin"** nella navbar (che è visibile solo agli staff/admin).
4. Naviga nella sezione `Store > Products` e aggiungi un nuovo prodotto (es. "Mouse Wireless"), impostando una categoria, un prezzo e una disponibilità (stock) di 10 pezzi.
5. Torna al sito cliccando su "View site" in alto a destra.
6. Clicca su **"Esci (Logout)"**.

### 2. Navigazione e Controllo Permessi (Ruolo Cliente)
1. Clicca su **"Accedi"** ed effettua il login con l'account **`cliente1`**.
2. **Test Permessi:** Verifica che il link "Pannello Admin" *non* sia più visibile nella navbar.
3. Clicca su **"Catalogo Prodotti"** e verifica la presenza del nuovo "Mouse Wireless" appena creato dall'admin.

### 3. Workflow di Acquisto e Verifica Risultati
1. Clicca su "Vedi Dettaglio" del "Mouse Wireless".
2. Clicca sul pulsante verde **"Aggiungi al Carrello"**.
3. Verrai reindirizzato al Carrello. Verifica che il Totale Parziale e il Totale Ordine siano calcolati correttamente.
4. Clicca sul pulsante nero **"Procedi al Pagamento Simulato"**.
5. **Verifica il risultato:** Atterrerai sulla pagina di successo ("Pagamento Ricevuto con Successo!"). 
6. Cliccando su "Torna al Catalogo", se torni nel dettaglio del "Mouse Wireless", vedrai che la disponibilità (stock) è diminuita di 1 unità, confermando l'aggiornamento del database post-checkout.