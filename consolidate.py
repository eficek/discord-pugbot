# Sends players from picking b channel to main picking
async def consolidate_pugs(message, picking_a, picking_b):
    for user in picking_b.members:
        try:
            # Moves user to picking
            await user.move_to(picking_a)
        except Exception as e:
            # When player fails to be moved, log error
            print(e)
            await message.channel.send(f'failed to move {user.name}')  # if fail, send this
    await message.channel.send('moved all puggers to picking')
