# 🛡️ VPN Domestica con WireGuard

<p align="center">
  <img height="110" src="https://images.icon-icons.com/2699/PNG/512/wireguard_logo_icon_167956.png">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20sviluppo-blue">
  <img src="https://img.shields.io/badge/Linux-Server-black">
  <img src="https://img.shields.io/badge/WireGuard-Active-red">
  <img src="https://img.shields.io/badge/Proxmox-Ready-orange">
  <img src="https://img.shields.io/badge/Use%20Case-Home%20Lab-green">
</p>

---

## 📌 0️⃣ Introduzione
Attraverso questa guida è possibile realizzare una **VPN domestica** per poter connettersi alla propria rete di casa (oppure di lavoro) anche da remoto. Per farlo utilizzeremo i seguenti servizi:
- Un servizio di DDNS (se non abbiamo un IP statico)
- Un server Linux (utilizzerò Debian)
- Un Proxmox Virtual Environment (facoltativo ma consigliatissimo)
- Wireguard
- Telegram per la creazione di un Bot

Per farlo avremo bisogno di:
- Una connessione internet con IP pubblico
- Un computer su cui eseguire Proxmox oppure direttamente il Server Linux
- Un computer da cui controlleremo Proxmox
- Un telefono con una connessione in rete dati per testare la VPN (o altri modi equivalenti)

---

## ⚠️ DISCLAIMER
Questo progetto è la messa in atto di quanto descritto nel video dell'utente ...  
L'obiettivo è quello di spiegare alcuni passaggi che sono stati saltati o affrontati troppo velocemente, arricchendoli con spiegazioni tecniche e approfondimenti didattici.

---

## 📚 Sommario
| Capitolo | Titolo | Link |
|--------|--------|------|
|0️⃣| **Introduzione** | Sei qui 👇 |
|1️⃣| Cosa faremo e cosa utilizzeremo | Da fare |
|2️⃣| Configurazione servizio DDNS | Da fare |
|3️⃣| Configurazione Container Linux Server | Da fare |
|4️⃣| Installazione Wireguard su Linux Server | Da fare |
|5️⃣| Apertura delle porte per Wireguard | Da fare |
|6️⃣| Configurazione del primo client |Da fare |
|7️⃣| Gestione dei client | Da fare |
|8️⃣| Attivare/Disattivare la VPN da remoto con Bot Telegram | Da fare |
|9️⃣| IMPORTANTE: Messa in sicurezza |Da fare|
|🔟| Considerazioni su affidabilità, prestazioni e sicurezza | Da fare |

---

# 📘 Concetti di base

## 🧠 Diamo prima alcune definizioni

### 🔹 Indirizzo IP – Internet Protocol
È un numero che identifica in modo univoco un nodo connesso a una rete. Esistono varie classi e tipologie, a noi interessa distinguere tra statico, dinamico, pubblico e CG-NAT. Queste tipologie di IP vengono assegnate dal nostro ISP (Internet Service Provider).

- **IP statico:** l'IP è sempre lo stesso e non cambia mai  
- **IP dinamico:** l'IP varia nel corso del tempo. Il cambio può avvenire in tempi e modi diversi (a discrezione dell'ISP oppure quando riavviamo il router)  
- **IP pubblico:** è l'IP con il quale siamo "conosciuti" in rete.  
- **IP CG-NAT – Carrier Grade NAT:**  
  a volte gli ISP non hanno abbastanza IP pubblici da fornire ai loro clienti. Per tanto forniscono lo stesso IP pubblico a più clienti: le connessioni private restano chiuse (non puoi accedere alla rete di un altro utente che ha il tuo stesso IP), ma la tua connessione passa attraverso una rete di livello superiore.  
  Un po' come se a casa tua avessi un ripetitore wifi: i dispositivi si collegano al ripetitore che a sua volta si collega al router principale.

---

## 🔁 NAT – Network Address Translation
È un servizio che permette a più dispositivi di condividere un unico indirizzo IP.

Pensiamo alla rete domestica:
- i router solitamente creano una rete domestica sull'indirizzo `192.168.0.1` oppure `192.168.1.1`
- tutti i dispositivi di casa avranno indirizzi a partire da `192.168.1.2` fino a `192.168.1.254`
- ma su Internet usciranno tutti con l'IP fornito dall'ISP

➡️ Il router si occupa quindi di tradurre l'indirizzo domestico (es. `192.168.1.210`) in quello della rete pubblica.

---

## 🔐 VPN – Virtual Private Network
Una VPN è un tunnel crittografato tra un utente e un server privato. Nel caso d'uso principale, quando un utente si connette a una VPN fa passare tutto il suo traffico attraverso questo tunnel.

```mermaid
flowchart LR
A[Ciro è connesso a internet con IP Pubblico XX.XX.XX.XX] --> B((TUNNEL VPN))
B --> C[Tutto il traffico di Ciro è indirizzato alla VPN. Ciro è su internet con indirizzo YY.YY.YY.YY]
```
In questo modo, l'utente sarà connesso a Internet, ma il suo traffico passa prima nel tunnel e dopo esce sulla rete.

---

## 🧰 Cosa ci serve per questo progetto:
- Una connessione con **IP statico** o **IP pubblico**

L'IP statico nella maggioranza dei casi è a pagamento e va richiesto, quindi controllate se avete un IP pubblico. Per farlo avete diversi modi:
- chiederlo direttamente al vostro ISP  
- accedere al vostro router e copiare l'IP indicato in "IP WAN" o altre voci simili e confrontarlo con quello che vi appare visitando un sito che mostra il vostro IP (basta cercare "my IP" su internet e aprire uno dei risultati)  
- se il vostro IP è nella fascia da `100.64.0.0` a `100.127.255.255` molto probabilmente è un IP sotto CG_NAT  
- da terminale digitare: `tracert [tuo_ip_pubblico]` e verificare i risultati.  
Se c'è un solo passaggio si ha IP pubblico, altrimenti è sotto CG-NAT.

---

## ⚠️ AVVISO IMPORTANTE
Se il tuo IP non è pubblico, chiama il tuo ISP e chiedi di fornirti un IP pubblico. Se dovessero dirti che non è disponibile, valuta di passare a un IP statico.  Se si tratta di un prezzo ragionevole (pochi euro in più al mese) puoi ottenere diverse funzionalità tra cui:
- realizzare questo progetto  
- migliorare la qualità del gaming online (la tua connessione sarebbe in NAT2, cerca su internet i vantaggi del NAT2 rispetto al NAT3 nel gaming)  
- utilizzo dell'IP statico per altri progetti (sorveglianza, cloud, hosting di pagine web e altro)

Puoi anche sottoscriverlo per qualche mese, testarlo e poi trarre le tue conclusioni.  
Magari nel mentre puoi cercare un altro ISP in grado di fornirti gratuitamente un IP pubblico.

---

## ⚠️ Attenzione
In realtà è possibile completare questo progetto anche con un IP non pubblico, ma ciò prevede l'utilizzo e la configurazione di altri sistemi (Virtual Private Server) che non sono trattati in questa guida. In pratica creerai una nuova VPN dalla tua connessione di casa a un server pubblico (molto spesso queste soluzioni sono a pagamento) e potrai quindi ottenere un ponte tra la tua connessione di casa e un punto di accesso pubblico.

---



