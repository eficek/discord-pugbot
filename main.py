import discord
import os
from keep_alive import keep_alive

client = discord.Client()
GUILD, TEST_VC, BLU_VC, RED_VC, BLU_VC_2, RED_VC_2, PICKING_VC, ANNOUNCE, DLPHN = (None, ) * 9


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    # this is so ugly, i need to brush up on py
    global GUILD, TEST_VC, BLU_VC, RED_VC, BLU_VC_2, RED_VC_2, PICKING_VC, ANNOUNCE, DLPHN
    GUILD = client.guilds[0]
    TEST_VC = GUILD.get_channel(658490352189046788)
    BLU_VC = GUILD.get_channel(727398699545788457)
    RED_VC = GUILD.get_channel(727395561401221219)
    BLU_VC_2 = GUILD.get_channel(819059052151439381)
    RED_VC_2 = GUILD.get_channel(819059106647375923)
    PICKING_VC = GUILD.get_channel(799692712797536296)
    ANNOUNCE = GUILD.get_channel(727395194714193980)
    DLPHN = await GUILD.fetch_member(233036215610245120)


@client.event
async def on_message(message):
    if message.channel.id == 825856008282701824:  # only allow commands in commands channel
        if message.author == client.user:
            return
        if message.content.startswith('!'):
            if message.content.startswith('!helloworld'):
                await message.channel.send('hello world')
            elif message.content.startswith('!help'):
                await message.channel.send('see pinned :)')
            elif message.content.startswith('!aconnect'):
                await a_connect(message)
            elif message.content.startswith('!bconnect'):
                await b_connect(message)
            elif message.content.startswith('!endpug'):
                await teams_to_picking(message)
            elif message.content.startswith(
                    '!fatkids') or message.content.startswith('!fk'):
                await post_fatkids(message)


async def a_connect(message):
    list = message.content.split()
    if len(list) == 3:
        for user in RED_VC.members:
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')
        for user in BLU_VC.members:
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')
        await message.channel.send(
            f'connect sent: steam://connect/{list[1]}/{list[2]}')
    else:
        await message.channel.send(
            'it appears the submitted info is not formatted correctly, be sure to submit in the form of "!aconnect [ip:port] [password]"'
        )

async def b_connect(message):
    list = message.content.split()
    if len(list) == 3:
        for user in RED_VC_2.members:
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')
        for user in BLU_VC_2.members:
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')
        await message.channel.send(
            f'connect sent: steam://connect/{list[1]}/{list[2]}')
    else:
        await message.channel.send(
            'it appears the submitted info is not formatted correctly, be sure to submit in the form of "!aconnect [ip:port] [password]"'
        )

async def teams_to_picking(message):
    for user in RED_VC.members:
        try:
            await user.move_to(PICKING_VC)
        except Exception as e:
            print(e)
            await message.channel.send(f'failed not move {user.name}')
    for user in BLU_VC.members:
        try:
            await user.move_to(PICKING_VC)
        except Exception as e:
            print(e)
            await message.channel.send(f'failed not move {user.name}')
    await message.channel.send('teams moved to picking')


async def post_fatkids(message):
    try:
        str = 'FK: '
        for user in PICKING_VC.members:
            str += f'{user.display_name}, '
        if len(str) > 4:
            await ANNOUNCE.send(str[:-2])
        else:
            await message.channel.send(
                'there appear to be no fatkids in channel')
    except Exception as e:
        print(e)
        await message.channel.send(
            f'{DLPHN.mention} exception occured, logged to console.')


keep_alive()
client.run(os.getenv('TOKEN'))
