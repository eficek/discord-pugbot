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
    TEST_VC = GUILD.get_channel(658490352189046788)                 # applies channel ID's - IF A CHANNEL GETS DELETED FIX THIS
    BLU_VC = GUILD.get_channel(727398699545788457)
    RED_VC = GUILD.get_channel(727395561401221219)
    BLU_VC_2 = GUILD.get_channel(819059052151439381)
    RED_VC_2 = GUILD.get_channel(819059106647375923)
    PICKING_VC = GUILD.get_channel(799692712797536296)
    ANNOUNCE = GUILD.get_channel(727395194714193980)
    DLPHN = await GUILD.fetch_member(233036215610245120)


# --------------------------------------------------------------------------------------------------------------------------
# begin msg definitions

@client.event
async def on_message(message):
    if message.channel.id == 825856008282701824:                                # only allow commands in commands channel
        if message.author == client.user:		
            return
        if message.content.startswith('!'):                                     # check for cmd send
            if message.content.startswith('!helloworld'):
                await message.channel.send('hello world')
            elif message.content.startswith('!help'):                           # help msg
                await message.channel.send('see pinned :)')
            elif message.content.startswith('!aconnect'):		                # sends connect for A Pugs
                await a_connect(message)
            elif message.content.startswith('!bconnect'):		                # sends connect for B Pugs
                await b_connect(message)
            elif message.content.startswith('!endapug'):			                # ends A pug
                await a_teams_to_picking(message)
            elif message.content.startswith('!endbpug'):                        # ends B pug
                await b_teams_to_picking(message)
            elif message.content.startswith(
                    '!fatkids') or message.content.startswith('!fk'):	        # sends fatkids msg
                await post_fatkids(message)

# end msg definitions
# --------------------------------------------------------------------------------------------------------------------------
# begin for (!aconnect) command

async def a_connect(message):						                            # first function: sends A connect
    list = message.content.split()                                              # splits connect msg into array
    if len(list) == 3:
        for user in RED_VC.members:                                             # do this for all users in RED_1 VC
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',         # send connect msg as link, del after 10 minutes
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')   # if user has DM's off, send this to runners
        for user in BLU_VC.members:                                             # do the same for BLU_1 vc
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')
        await message.channel.send(
            f'connect sent: steam://connect/{list[1]}/{list[2]}')               # wait for msg to be sent correctly
    else:
        await message.channel.send(                                             # if msg is formatted wrong, send this
            'it appears the submitted info is not formatted correctly, be sure to submit in the form of "!aconnect [ip:port] [password]"'
        )     

# end for (!aconnect) command
# --------------------------------------------------------------------------------------------------------------------------
# begin for (!bconnect) command

async def b_connect(message):						# second function: sends B connect - functionally identical to a_connect
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

# end for (!bconnect) command
# --------------------------------------------------------------------------------------------------------------------------
# begin for (!endpug) commands

# a pugs

async def a_teams_to_picking(message):					                    # third function: sends a teams back to picking
    for user in RED_VC.members:
        try:
            await user.move_to(PICKING_VC)                                  # move user to channel
        except Exception as e:
            print(e)
            await message.channel.send(f'failed not move {user.name}')      # if fail, send this
    for user in BLU_VC.members:
        try:
            await user.move_to(PICKING_VC)
        except Exception as e:
            print(e)
            await message.channel.send(f'failed not move {user.name}')
    await message.channel.send('teams moved to picking')                    # if successful, send this

# b pugs endpug

async def b_teams_to_picking(message):                                      # fourth function: sends b teams back to picking - functionally identical to a_teams_to_picking
    for user in RED_VC_2.members:
        try:
            await user.move_to(PICKING_VC)                                  
        except Exception as e:
            print(e)
            await message.channel.send(f'failed not move {user.name}')      
    for user in BLU_VC_2.members:
        try:
            await user.move_to(PICKING_VC)
        except Exception as e:
            print(e)
            await message.channel.send(f'failed not move {user.name}')
    await message.channel.send('teams moved to picking')                    


# end for (!endpug) commands
# --------------------------------------------------------------------------------------------------------------------------
# begin for (!fk / !fatkids) command

async def post_fatkids(message):					                        # fourth function: sends fatkid names 
    try:
        str = 'FK: '                                                        # define beg of string
        for user in PICKING_VC.members:                                     # do for all users left in picking after pug starts
            str += f'{user.display_name}, '                                 # add user to string
        if len(str) > 4:
            await ANNOUNCE.send(str[:-2])
        else:
            await message.channel.send(
                'there appear to be no fatkids in channel')                 # if no fatkids, send this
    except Exception as e:
        print(e)
        await message.channel.send(
            f'{DLPHN.mention} exception occured, logged to console.')       # catch exception, alert those responsible

# end for (!fk / !fatkids) command
# --------------------------------------------------------------------------------------------------------------------------


keep_alive()                                                                # abuses free system for gain
client.run(os.getenv('TOKEN'))