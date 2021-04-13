async def send_connect(message, red, blu):						                              # first function: sends A connect
    list = message.content.split()                                              # splits connect msg into array
    if len(list) == 3:
        for user in red.members:                                                # do this for all users in RED_1 VC
            try:
                await user.send(f'steam://connect/{list[1]}/{list[2]}',         # send connect msg as link, del after 10 minutes
                                delete_after=600)
            except Exception as e:
                print(e)
                await message.channel.send(
                    f'{user.name} appears to have dms off, connect not sent')   # if user has DM's off, send this to runners
        for user in blu.members:                                                # do the same for BLU_1 vc
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