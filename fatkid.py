# Checks for the fatkids and prints them to pug_announcements
async def post_fatkids(message, picking, announce, guild):
    DLPHN = await guild.fetch_member(233036215610245120)
    GRRT = await guild.fetch_member(115328914552782857)
    try:
        fatkids = []
        # Add all users left in picking to list of fatkids
        for user in picking.members:
            fatkids.append(user.display_name)

        # If there were any fatkids found, print
        if len(fatkids) > 0:
            str = 'FK: ' + ', '.join(fatkids)
            await announce.send(str)
        else:
            await message.channel.send('there appear to be no fatkids in channel')
    except Exception as e:
        # error handling
        print(e)
        await message.channel.send(f'{await DLPHN.mention} {await GRRT.mention} exception occurred, logged to console.')
