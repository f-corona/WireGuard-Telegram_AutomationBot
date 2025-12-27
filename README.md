# VPN-domestica-con-WireGuard
Implementazione di una VPN domestica con WireGuard su server Linux (in esecuzione su Proxmox). Il progetto consente l’accesso sicuro alla connessione di casa da remoto. Nelle varie fasi vengono spiegati vari concetti relativi al routing, sicurezza di rete, gestione delle chiavi e automazione tramite servizi terzi.

# 🛡️ Infrastruttura VPN Domestica con WireGuard su Linux

![status](https://img.shields.io/badge/Stato-In%20sviluppo-blue)
![Linux](https://img.shields.io/badge/Linux-Server-black)
![WireGuard](https://img.shields.io/badge/WireGuard-VPN-red)
![Proxmox](https://img.shields.io/badge/Hosted%20on-Proxmox-orange)

---

Attraverso questa guida è possibile realizzare una **VPN domestica sicura** per connettersi alla propria rete di casa (oppure di lavoro) anche da remoto.

---

## ⚠️ Disclaimer / Riconoscimenti
Questo progetto è la messa in atto di quanto descritto nel video dell'utente **USER**.  
L'obiettivo è quello di spiegare alcuni passaggi che nel video originale vengono saltati o affrontati troppo velocemente, aggiungendo spiegazioni, struttura e chiarimenti per chi vuole imparare davvero come funziona una VPN domestica.

---

## 📚 Indice
- [Introduzione](#-introduzione)
- [Definizioni di base](#-diamo-prima-alcune-definizioni)
- [NAT](#-nat--network-address-translation)
- [Cosè una VPN](#-vpn--virtual-private-network)
- [Requisiti di rete](#-cosa-ci-serve-per-questo-progetto)
- [Come verificare se hai IP pubblico](#-come-verificare-se-hai-ip-pubblico)
- [Avvisi importanti](#-avviso-importante)
- [Alternativa senza IP pubblico](#-avviso-importante--alternativa-senza-ip-pubblico)

---

## 🧠 Introduzione
Lo scopo di questo progetto è permettere a chiunque di:
✔️ accedere alla propria rete domestica da remoto  
✔️ utilizzare dispositivi come NAS, DVR, stampanti, server, PC domestici  
✔️ migliorare la sicurezza e il controllo della rete  
✔️ imparare davvero come funziona una VPN

Questa non è una guida "plug & play", ma un percorso **didattico**.

---

## 📘 Diamo prima alcune definizioni

### 🔹 Indirizzo IP – Internet Protocol
È un numero che identifica in modo univoco un nodo connesso a una rete.

Ci interessa distinguere tra:

- **IP statico** → l'IP è sempre lo stesso e non cambia mai  
- **IP dinamico** → l'IP varia nel tempo (deciso dall’ISP o quando riavvii il router)  
- **IP pubblico** → è l'indirizzo con cui “appari” su Internet  
- **IP CG-NAT – Carrier Grade NAT**  
  Gli ISP, quando non hanno abbastanza IP pubblici, assegnano lo stesso IP a più utenti.  
  Le reti restano separate, ma il tuo traffico passa attraverso una rete “superiore”.

📌 È paragonabile a un ripetitore Wi-Fi:  
ti colleghi al ripetitore → che a sua volta si collega al router → che infine esce in Internet.

---

## 🔁 NAT – Network Address Translation
Permette a più dispositivi di condividere un unico indirizzo IP.

Esempio rete domestica:

- rete locale: `192.168.0.x` o `192.168.1.x`
- i dispositivi usano IP interni
- all’esterno escono tutti con **lo stesso IP pubblico**

➡️ Il router traduce (“traduce”) gli indirizzi interni → in un solo indirizzo pubblico.

---

## 🕳️ VPN – Virtual Private Network
Una **VPN è un tunnel crittografato** tra un client e un server privato.

Quando ti connetti:
- il traffico passa prima dentro il tunnel
- solo dopo esce in Internet
- oppure accede direttamente alla rete domestica

### 🖼️ Schema concettuale
```mermaid
flowchart LR
A[CLIENTE] --> B((TUNNEL VPN))
B --> C[RETE DI CASA]
