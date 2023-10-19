import discord
import responses
import random
import string



async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'TOKEN_NAME HERE!'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        p_message = message.content.lower()

        if p_message == '!ping':
            await message.channel.send('`pong` :ping_pong: ')
        elif p_message == '!pong':
            await message.channel.send('`ping` :ping_pong: ')
        elif isinstance(message.channel, discord.DMChannel) and p_message == '!id':
            await message.author.send(f"Your Discord ID is {message.author.id}")
        elif p_message in ['!hey', '!yo', '!hi', '!hello']:
            await message.channel.send(f'Hey there {message.author.name} :wave:')
        elif p_message == '!roll':
            roll = random.randint(1, 6)
        elif p_message == '!highroll':
            user_roll = random.randint(1, 6)
            bot_roll = random.randint(1, 6)

            await message.channel.send(f'You rolled a {user_roll} :game_die:')
            await message.channel.send(f'Expresso Depresso rolled a {bot_roll} :game_die:')

            if user_roll > bot_roll:
                await message.channel.send('You win! :trophy:')
            elif user_roll < bot_roll:
                await message.channel.send('Expresso Depresso wins! :dotted_line_face: ')
            else:
                await message.channel.send('It\'s a tie! :flag_white:')

        elif message.author.id == 319526449851793420 and p_message == '!type':
            await message.channel.send(f'Hey {message.author.name}!')
        elif message.author.id == 571371776114688020 and p_message == '!type':
            await message.channel.send(f'Hey {message.author.name}!')
        elif message.author.id == 485738324032618497 and p_message == '!type':
            await message.channel.send(f'Hey {message.author.name}!')
        elif message.author.id == 439462455618437120 and p_message == '!type':
            await message.channel.send(f'Hey {message.author.name}!')
        elif p_message == '!break':
            await message.channel.send('!break')
        elif p_message == '!name':
            await message.channel.send(f"Your name is {message.author.display_name}")
        elif p_message == '!my_id':
            await message.channel.send(f'Hey there {message.author.name}! Your Discord ID is {message.author.id}')
        elif p_message == "!blackjack":
            if message.author.bot:
                await message.channel.send("Sorry, only human players can play blackjack.")
                return

            def calculate_hand_value(hand):
                value = 0
                aces = 0
                for card in hand:
                    if card == "A":
                        aces += 1
                    elif card in ["K", "Q", "J"]:
                        value += 10
                    else:
                        value += int(card)
                for i in range(aces):
                    if value + 11 <= 21:
                        value += 11
                    else:
                        value += 1
                return value

            async def get_player_action(channel):
                while True:
                    await channel.send("Do you want to hit or stand? (h/s) :punch: or :man_standing: ")
                    response = await client.wait_for("message")
                    if response.author == client.user:
                        continue
                    if response.content.lower() in ["hit", "h"]:
                        return "hit"
                    elif response.content.lower() in ["stand", "s"]:
                        return "stand"
                    else:
                        await channel.send("Invalid action. Please enter 'hit' or 'stand'. :punch: or :man_standing: ")
                        continue


            deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
            random.shuffle(deck)

            player_hand = []
            dealer_hand = []

            # deal initial cards
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

            # calculate hand values
            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)

            # show initial hands
            await message.channel.send(f"Your hand: {player_hand} (value: {player_value})")
            await message.channel.send(f"Dealer's hand: [{dealer_hand[0]}, ?] :robot: ")

            # player's turn
            while True:
                action = await get_player_action(message.channel)
                if action == "hit":
                    player_hand.append(deck.pop())
                    player_value = calculate_hand_value(player_hand)
                    await message.channel.send(f"You drew {player_hand[-1]} (value: {player_value})")
                    if player_value > 21:
                        await message.channel.send("Bust! You lose. :dotted_line_face:")
                        return
                else:
                    break

            # dealer's turn
            while dealer_value < 17:
                dealer_hand.append(deck.pop())
                dealer_value = calculate_hand_value(dealer_hand)
                await message.channel.send(f"Dealer drew {dealer_hand[-1]} (value: {dealer_value})")
                if dealer_value > 21:
                    await message.channel.send("Dealer bust! You win. :trophy:")
                    return

            # compare hands
            if player_value > dealer_value:
                await message.channel.send("You win! :trophy:")
            elif player_value < dealer_value:
                await message.channel.send("Dealer wins! :dotted_line_face:")
            else:
                await message.channel.send("It's a tie! :flag_white:")

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

            # Define the channel ID
            channel_id = 1234567890, 981918394653749269

            # Get the channel object using the ID
            channel = client.get_channel(channel_id)

    client.run(TOKEN)
