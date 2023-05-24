import discord
import random
import bot
import main

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!invite':
        return f'Here is your invite! https://discord.gg/YdGpYNQf'

    if p_message == '!いいえ':
        return 'No!'

    if p_message == '!はい':
        return 'Yes!'

    if p_message == '!help':
        return '`Try these following commands with the prefix !, "ping, pong, bitch, my_id, hey, いいえ, yo, はい, roll, name, hell, highroll, blackjack, tell.`'