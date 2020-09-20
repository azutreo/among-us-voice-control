import discord
import config

PRODUCTION = config.PRODUCTION
PRODUCTION_TOKEN = config.PRODUCTION_TOKEN
DEVELOPMENT_TOKEN = config.DEVELOPMENT_TOKEN

class DiscordClient(discord.Client):
	async def on_ready(self):
		print("Logged on as {0}!".format(self.user))

		game = discord.Game("with Nicholas Foreman")
		await self.change_presence(activity = game)

	async def on_message(self, message):
		if message.author.bot:
			return

		content = message.content

		if content == None:
			return
		elif len(content) <= 0:
			return

		arguments = content.split()

		if arguments[0].find('a!', 0, 2) == -1:
			return

		if arguments[0] == "a!help":
			embed = discord.Embed()
			embed.title = "Among Us Voice Control - Help"
			embed.color = discord.Color.green()
			embed.add_field(name = "Prefix", value = "`a!`", inline = False)
			embed.add_field(name = "Required Permission to Use Commands", value = "Manage Channels", inline = False)
			embed.add_field(name = "Commands",
				value = """
				`a!mutechannel` - Overrides the speak permission to **`false`** for the \@everyone role for the channel the user is in
				`a!unmutechannel` - Overrides the speak permission to **`none`** for the \@everyone role for the channel the user is in""",
				inline = False)

			await message.channel.send(embed = embed)

			return

		embed = discord.Embed()

		permissions = message.channel.permissions_for(message.author)
		if not permissions.manage_channels:
			embed.color = discord.Color.red()
			embed.description = "You do not have permission to do that"

			return await message.channel.send(embed = embed)

		everyoneRole = message.guild.default_role

		if arguments[0] == "a!mutechannel":
			voiceChannel = message.author.voice
			if not voiceChannel:
				embed.color = discord.Color.red()
				embed.description = "You are not in a voice channel"

				return await message.channel.send(embed = embed)

			voiceChannel = voiceChannel.channel
			if not voiceChannel:
				embed.color = discord.Color.red()
				embed.description = "You are not in a voice channel"

				return await message.channel.send(embed = embed)

			async with message.channel.typing():
				await voiceChannel.set_permissions(everyoneRole, speak = False)

				for member in voiceChannel.members:
					await member.move_to(voiceChannel)

				embed.color = discord.Color.green()
				embed.description = "Muted channel"
				return await message.channel.send(embed = embed)
		elif arguments[0] == "a!unmutechannel":
			voiceChannel = message.author.voice
			if not voiceChannel:
				embed.color = discord.Color.red()
				embed.description = "You are not in a voice channel"

				return await message.channel.send(embed = embed)

			voiceChannel = voiceChannel.channel
			if not voiceChannel:
				embed.color = discord.Color.red()
				embed.description = "You are not in a voice channel"

				return await message.channel.send(embed = embed)

			async with message.channel.typing():
				await voiceChannel.set_permissions(everyoneRole, speak = None)

				for member in voiceChannel.members:
					await member.move_to(voiceChannel)

				embed.color = discord.Color.green()
				embed.description = "Unmuted channel"
				return await message.channel.send(embed = embed)
		else:
			return

client = DiscordClient()

if PRODUCTION:
	client.run(PRODUCTION_TOKEN)
else:
	client.run(DEVELOPMENT_TOKEN)