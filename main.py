from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import requests

# Replace with your bot's API Token and target bot's username
MY_BOT_TOKEN = "7532369778:AAE-fyhEq-pEAC8ChuMVC2mXz41zDQb_GoA"
TARGET_BOT_USERNAME = "@SpamBot"  # Target bot's username

# Telegram API URL
MY_BOT_API_URL = f"https://api.telegram.org/bot{MY_BOT_TOKEN}"


def forward_message_to_target_bot(user_message: str) -> dict:
    """Forward the user's message to the target bot."""
    try:
        response = requests.post(
            f"{MY_BOT_API_URL}/sendMessage",
            data={"chat_id": TARGET_BOT_USERNAME, "text": user_message},
        )
        return response.json()
    except Exception as e:
        return {"ok": False, "error": str(e)}


def handle_message(update: Update, context: CallbackContext):
    """Handle all messages from the user."""
    user_message = update.message.text
    chat_id = update.message.chat_id

    # Forward the message to the target bot
    target_response = forward_message_to_target_bot(user_message)

    if target_response.get("ok"):
        context.bot.send_message(chat_id=chat_id, text=target_response["result"]["text"])
    else:
        context.bot.send_message(chat_id=chat_id, text="Error: Unable to get a response from the target bot.")


def main():
    """Run the proxy bot."""
    updater = Updater(MY_BOT_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
