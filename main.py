import discord
import os
from keep_alive import keep_alive

client = discord.Client()
GUILD = None
TEST_VC = None
BLU_VC = None
RED_VC = None
PICKING_VC = None
DLPHN = None


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    # this is so ugly, i need to brush up on py
    global GUILD
    global TEST_VC
    global BLU_VC
    global RED_VC
    global PICKING_VC
    global DLPHN
    GUILD = client.guilds[0]
    TEST_VC = GUILD.get_channel(658490352189046788)
    BLU_VC = GUILD.get_channel(727398699545788457)
    RED_VC = GUILD.get_channel(727395561401221219)
    PICKING_VC = GUILD.get_channel(799692712797536296)
    DLPHN = await GUILD.fetch_member(233036215610245120)


@client.event
async def on_message(message):
    if message.channel.id == 825856008282701824:
        if message.author == client.user:
            return
        if message.content.startswith('!'):
            if message.content.startswith('!helloworld'):
                await message.channel.send('hello world')
            elif message.content.startswith('!connect'):
                await connect(message, message.content[9:])
            elif message.content.startswith('!endpug'):
                await teams_to_picking(message)


async def connect(message, info):
    try:
        for user in RED_VC.members:
            await user.send(info)     
        for user in BLU_VC.members:
            await user.send(info)
        await message.channel.send('connect sent: ' + message.content[9:])
    except Exception as e:
        print(e)
        await message.channel.send(DLPHN.mention +
                                   ' exception occured, logged to console.')
    return


async def teams_to_picking(message):
    try:
        for user in RED_VC.members:
            await user.move_to(PICKING_VC)
        for user in BLU_VC.members:
            await user.move_to(PICKING_VC)
        await message.channel.send('teams moved to picking')
    except Exception as e:
        print(e)
        await message.channel.send(DLPHN.mention +
                                   ' exception occured, logged to console.')
    return


keep_alive()
client.run(os.getenv('TOKEN'))
