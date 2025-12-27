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
|0️⃣| Introduzione | Link |
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



