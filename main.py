import telegram
import os

# Inserisci il tuo token di accesso del bot qui
bot_token = "5851242241:AAHIma5P17jjXpr1zp7w_4H67tXaC_QZUCg"

# Inserisci l'ID del tuo canale qui
channel_id = -1574460808

bot = telegram.Bot(token=bot_token)

# Funzione per inviare un messaggio anonimo al canale
def send_anon_message(text):
  # Invia il messaggio al canale come il bot
  bot.send_message(chat_id=channel_id, text=text, disable_notification=True)

# Funzione per gestire i messaggi ricevuti dal bot
def handle_messages(messages):
  for message in messages:
    # Controlla se il messaggio è stato inviato da un utente privato
    if message.chat.type == "private":
      # Invia il messaggio al canale come messaggio anonimo
      send_anon_message(message.text)

# Esegue il loop principale del bot
while True:
  # Controlla i messaggi ricevuti dal bot
  handle_messages(bot.get_updates())
