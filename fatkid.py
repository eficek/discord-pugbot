async def post_fatkids(message, picking, announce, guild):					                        # third function: sends fatkid names 
    try:
        str = 'FK: '                                                        # define beg of string
        for user in picking.members:                                     # do for all users left in picking after pug starts
            str += f'{user.display_name}, '                                 # add user to string
        if len(str) > 4:
            await announce.send(str[:-2])
        else:
            await message.channel.send(
                'there appear to be no fatkids in channel')                 # if no fatkids, send this
    except Exception as e:
        print(e)
        await message.channel.send(
            f'{await guild.fetch_member(233036215610245120).mention} {await guild.fetch_member(115328914552782857).mention} exception occurred, logged to console.')       # error handling
        
