import os

import discord

from connect import send_connect
from endpug import teams_to_picking
from fatkid import post_fatkids
from keep_alive import keep_alive
from consolidate import consolidate_pugs

# import timeout

client = discord.Client()
REPORT_CHANNEL_ID = 841836172572885002
REPORT_CHANNEL = None
COMMAND_CHANNEL_ID = 825856008282701824
GUILD, TEST_VC, BLU_VC, RED_VC, BLU_VC_2, RED_VC_2, PICKING_VC, PICKING_VC_2, CLOWN_CAR, ANNOUNCE = (None,) * 10

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

    # this is so ugly, i need to brush up on py

    # TODO: Run these commands at command time, might solve bug where cannot move players in channel prior
    global GUILD, TEST_VC, BLU_VC, RED_VC, BLU_VC_2, RED_VC_2, PICKING_VC, PICKING_VC_2, CLOWN_CAR, ANNOUNCE, REPORT_CHANNEL
    GUILD = client.guilds[0]
    TEST_VC = GUILD.get_channel(658490352189046788)  # applies channel ID's - IF A CHANNEL GETS DELETED FIX THIS
    BLU_VC = GUILD.get_channel(727398699545788457)
    RED_VC = GUILD.get_channel(727395561401221219)
    BLU_VC_2 = GUILD.get_channel(819059052151439381)
    RED_VC_2 = GUILD.get_channel(819059106647375923)
    PICKING_VC = GUILD.get_channel(799692712797536296)
    PICKING_VC_2 = GUILD.get_channel(819058981870895105)
    CLOWN_CAR = GUILD.get_channel(819804916859011082)
    ANNOUNCE = GUILD.get_channel(727395194714193980)
    REPORT_CHANNEL = GUILD.get_channel(REPORT_CHANNEL_ID)
    # DLPHN = await GUILD.fetch_member(233036215610245120)
    # GRRT = await GUILD.fetch_member(115328914552782857)
    # Rebel = await GUILD.fetch_member(160225394526519296)

# --------------------------------------------------------------------------------------------------------------------------
# begin msg definitions

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.channel.id == COMMAND_CHANNEL_ID:  # only allow commands in commands channel
        if message.author == client.user:
            return
        if not message.content.startswith('!'):  # check for cmd send
            return

        if message.content.startswith('!helloworld'):
            await message.channel.send('hello world')
        elif message.content.startswith('!help'):  # help msg
            await message.channel.send('see pinned :)')
        elif message.content.startswith('!connect'):  # sends connect for A Pugs
            await send_connect(message, RED_VC, BLU_VC)
        elif message.content.startswith('!bconnect'):  # sends connect for B Pugs
            await send_connect(message, RED_VC_2, BLU_VC_2)
        elif message.content.startswith('!endpug'):  # ends A pugs
            await teams_to_picking(message, RED_VC, BLU_VC, PICKING_VC)
        elif message.content.startswith('!endbpug'):  # ends B pugs
            await teams_to_picking(message, RED_VC_2, BLU_VC_2, PICKING_VC_2)
        elif message.content.startswith('!consolidate'):
            await consolidate_pugs(message, PICKING_VC, PICKING_VC_2)
        elif message.content.startswith('!fatkids') or message.content.startswith('!fk'):  # sends fatkids msg
            await post_fatkids(message, PICKING_VC, ANNOUNCE, GUILD)
        elif message.content.startswith('!timeout'):
            pass
    elif isinstance(message.channel, discord.DMChannel):
        if message.content.startswith('!clear'):
            history = message.channel.history(limit=1000)
            async for message in history:
                if message.author.id == client.user.id:
                    await message.delete()
        else:
            await message.channel.send('Report Submitted.', delete_after=30)
            await REPORT_CHANNEL.send(f'{message.author.name}: {message.content}')


keep_alive()  # abuses free system for gain
client.run(os.getenv('TOKEN'))
