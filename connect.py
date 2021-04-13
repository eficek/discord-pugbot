# Sends connect to members of channel 1 and channel 2
async def send_connect(message, team1, team2):  # first function: sends A connect
    command = message.content.split()  # splits connect msg into array
    if len(command) == 3:
        # command is in the format '!connect ip password'
        ip, password = command[1], command[2]
        users = team1.members + team2.members

        # Sends DM to all users
        for user in users:
            try:
                # Send connect msg as link, del after 10 minutes
                await user.send(f'steam://connect/{ip}/{password}', delete_after=600)
            except Exception as e:
                # Exception if user has DM's off, send this to runners
                print(e)
                await message.channel.send(f'{user.name} appears to have dms off, connect not sent')
    else:
        # if msg is formatted wrong, send this
        usage_message = 'it appears the submitted info is not formatted correctly, be sure to submit in the form of ' \
                        f'"!connect [ip:port] [password]" '
        await message.channel.send(usage_message)
