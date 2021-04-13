async def timeout(message, destination, guild):
	list = message.content.split()																						# split the message into array
	if len(list) > 1:																									# make sure there's a user in the argument
		try:
			for user in range(:1):																						
				try:
					await user.move_to(CLOWN_CAR)																		# move the user(s)
				except Exception as e:
					print(e)
					await message.channel.send(f'Failed to move {user.name}.')											# in case the user leaves or smthn
				try:
					await user.send(f"you have been placed in time out, noob")								# DM this to the user(s)
				except Exception as e:
					print(e)
					await message.channel.send(f'Failed to message {user.name}')										# if the user has DMs off
			await message.channel.send(f'User {user.name} has been sat out.')											# confirmation msg
		else:
			await message.channel.send(f'Error: No username input. Format: `!timeout [user] [user2] ...`')				# wrong formatting from runner
		except Exception as e
		print(e)
		await message.channel.send(
			f'{await guild.fetch_member(233036215610245120).mention} {await guild.fetch_member(115328914552782857).mention} exception occurred, logged to console.')									# error handling

	

