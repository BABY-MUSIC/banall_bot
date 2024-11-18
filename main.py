from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, CallbackContext

# Replace with your own values
MY_BOT_TOKEN = "7532369778:AAE-fyhEq-pEAC8ChuMVC2mXz41zDQb_GoA"  # Your bot's API token
TARGET_BOT_USERNAME = "@EnhancerOPbot"  # Target bot's username

# Replace with your API ID, API Hash, and string session
api_id = "16457832"  # Your API ID from Telegram
api_hash = "3030874d0befdb5d05597deacc3e83ab"  # Your API Hash from Telegram
string_session = "BQD7IGgAU01QJJfd2Pqwr4mcAlKnateLPNSe4LkrGmGOY7IpnQFk2GBAeZzAPOH4wEhSFArwbMv7G4zmEgBtvTGVAWmNk05cNgy6HC6Q8eDvFAjc8ED9qeq9ERkSulSklJOwWoGzZx7VVLSNE2cOd4K2-aiL-wrNcC_QjAN_FcI6GNrDzZZdvtORvNzSxH_o3OucLvoIsRdt-rMSyikkJJMyELHdKETJCWVHQPfqR2t7IGUT0UrVYdfFKNZcwaqxqnK60jeRi3f6pUmXg11xhxNIawLXaKZc_hw5MoJ5KdkduLmW0Mtbh5anTWi8t1quXQvZhc4Mons8uvgRf-dwQRmPFtz8rgAAAAGpD8oQAA"  # String session from Telethon

# Create Telegram Client with session
with TelegramClient(StringSession(string_session), api_id, api_hash) as client:

    # Function to forward message to the target bot and get a response
    def forward_message_to_target_bot(user_message: str) -> str:
        """Send message to the target bot and receive the response."""
        try:
            # Send the message to target bot
            response = client.send_message(TARGET_BOT_USERNAME, user_message)
            return response.text  # Return the text response from the target bot
        except Exception as e:
            return f"Error: {str(e)}"

    # Function to handle user messages
    def handle_message(update: Update, context: CallbackContext):
        """Forward user message to target bot and send the response back to the user."""
        user_message = update.message.text  # Get user's message
        chat_id = update.message.chat.id  # Get user's chat ID

        # Forward the message to the target bot and get the response
        target_response = forward_message_to_target_bot(user_message)

        # Send the target bot's response back to the user
        if target_response:
            update.message.reply_text(target_response)
        else:
            update.message.reply_text("Error: Unable to get a response from the target bot.")

    # Main function to set up the bot
    def main():
        """Run the bot."""
        # Set up the Updater with your bot's API token
        updater = Updater(MY_BOT_TOKEN, use_context=True)

        # Set up the dispatcher to add handlers
        dp = updater.dispatcher

        # Add message handler for non-command text messages
        dp.add_handler(MessageHandler(filters.Text & ~filters.Command, handle_message))

        # Start polling for updates
        updater.start_polling()
        updater.idle()

    # Start the bot
    if __name__ == "__main__":
        main()
