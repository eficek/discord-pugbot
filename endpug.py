async def teams_to_picking(message, red, blu, picking):					                    # second function: sends teams back to picking
    for user in red.members:
        try:
            await user.move_to(picking)                                  # move user to channel
        except Exception as e:
            print(e)
            await message.channel.send(f'failed to move {user.name}')      # if fail, send this
    for user in blu.members:
        try:
            await user.move_to(picking)
        except Exception as e:
            print(e)
            await message.channel.send(f'failed to move {user.name}')
    await message.channel.send('teams moved to picking')                    # if successful, send this