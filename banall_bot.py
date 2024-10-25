from telethon import TelegramClient, events
import asyncio

# Yahan apna session string, API ID aur API hash daalein
api_id = '16457832'
api_hash = '3030874d0befdb5d05597deacc3e83ab'
session_string = 'BQD7IGgARS5xsaGsFFQkqnXg9UoH0VopFLBB7GkA3bRJmKv-bnT-JXqx-i5mUsj50rzPbQdUtlEhEcJVobhQkhLcgpfio9P0dwCeB84zdSB50n5bJLcCEChdi8dFF5uOtNynpaIZFbdEXhz9aKtjnRmnSncGc6k31QoQst0HVC0FO590nBQzAAsVQFo44sbTJZIngWZescLM21eWyG5qtwmIQWXV24Zp597JqwpIUvD-B0abhLNbMbnqCkZhUSfCmJox8KrZol7Oc9E2rudQpQ-XV71QOxYAt1xeDZLGVzt3T9M1byHHvR8ek_BBzKLMxmhNaOACorHJ0RkWNPRGpypB9jhASQAAAAGugN_jAA'

client = TelegramClient(session_string, api_id, api_hash)

@client.on(events.NewMessage(pattern=r'^\.banall$', outgoing=True))
async def ban_all(event):
    if event.is_group:
        count = 0
        async for user in client.iter_participants(event.chat_id):
            try:
                # User ko ban karte hain
                await client.edit_permissions(event.chat_id, user.id, view_messages=False)
                count += 1
                await asyncio.sleep(0.5)  # Delay to avoid flood wait; aap ise aur increase kar sakte hain

                # Har 200 members ban hone par 10 seconds wait
                if count % 200 == 0:
                    await asyncio.sleep(10)
                    
            except Exception as e:
                print(f"Error banning user {user.id}: {e}")

        await event.reply("21,000 members mein se sabhi ko ban kar diya gaya hai.")
    else:
        await event.reply("Ye command sirf group mein kaam karti hai.")

client.start()
client.run_until_disconnected()
