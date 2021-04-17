# Sends players from channels team1 and team2 to channel picking
async def teams_to_picking(message, team1, team2, picking):
    users = team1.members + team2.members
    for user in users:
        try:
            # Moves user to picking
            await user.move_to(picking)
        except Exception as e:
            # When player fails to be moved, log error
            print(e)
            await message.channel.send(f'failed to move {user.name}')  # if fail, send this
    await message.channel.send('teams moved to picking')
