import subprocess
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

#logging, lo utilizzeremo per la cronologia di attività del bot
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# configurazione dei dati telegram
TOKEN = "7XXXM" #token del bot da recuperare su botfather
AUTHORIZED_USER = XXXX #inserire id utente da recuperare

#interazione con il sistema operativo
#gli argomenti di subprocess.run sono i parametri con cui viene lanciato il bot
def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True) 
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Errore: {e.stderr.strip()}"


# confrontiamo l'id di chi scrive con quello
async def check_auth(update: Update):
    if update.effective_user.id != AUTHORIZED_USER:
        await update.message.reply_text("Accesso negato.")
        return False
    return True


#definiamo le azioni per i comandi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_auth(update): return
    await update.message.reply_text("Bot WireGuard Attivo\n/wg_on\n/wg_off")

async def wg_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_auth(update): return
    run_shell_command("systemctl start wg-quick@wg0")
    await update.message.reply_text("VPN accesa")

async def wg_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await check_auth(update): return
    run_shell_command("systemctl stop wg-quick@wg0")
    await update.message.reply_text("VPN spenta")


#inizializza il bot e rimane in ascolto di nuovi messaggi.
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    app.add_handler(CommandHandler("wg_on", wg_on))
    app.add_handler(CommandHandler("wg_off", wg_off))

    print("Bot partito")
    app.run_polling()
