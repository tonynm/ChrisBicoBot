import discord
import random

random.seed()
client = discord.Client()

@client.event 
async def on_ready(): #When bot has connected to the server, this message is displayed on console
	print('We have logged in as {0.user}'.format(client))
	
@client.event 
async def on_connect():
	game = discord.Game('cbhelp') #Displays the help commmand as the status
	await client.change_presence(activity=game)	
		
@client.event
async def on_message(message):
	if message.author == client.user:
		return
		
	if message.content.startswith('cbhello'): #Bot says hello
		await message.channel.send('Hello')
		
	if message.content.startswith('cbbico'): #Bot prints out an emoji
		await message.channel.send('<Insert Emoji ID>')
		
	if message.content.startswith('cb@'): #Mentions person in server
		await message.channel.send('<@Insert User ID> But where you at?')
		
	if message.content.startswith('cbcp'): #Bot says one of 19 available catchphrases
		number = random.randint(0, 18)
		if (number == 0):
			await message.channel.send('Shaking my head')
		elif (number == 1):
			await message.channel.send('Gotta do my dailies')
		elif (number == 2):
			await message.channel.send('Whatcha mean?')
		elif (number == 3):
			await message.channel.send('Pachinko Luck')
		elif (number == 4):
			await message.channel.send('Yeah, Yeah')
		elif (number == 5):
			await message.channel.send('The Hell?')
		elif (number == 6):
			await message.channel.send('What up. What up. What uuuuuup')
		elif (number == 7):
			await message.channel.send('What the hell, man')
		elif (number == 8):
			await message.channel.send('Hey, that\'s pretty good!')
		elif (number == 9):
			await message.channel.send('Do it')
		elif (number == 10):
			await message.channel.send('Yeah, alright')
		elif (number == 11):
			await message.channel.send('Now hold on')
		elif (number == 12):
			await message.channel.send('Wub, Wub, Wub')
		elif (number == 13):
			await message.channel.send('Wait a minute')
		elif (number == 14):
			await message.channel.send('You trying to play sum Fornite?')
		elif (number == 15):
			await message.channel.send('I forgot to watch Pawn Stars')
		elif (number == 16):
			await message.channel.send('You crazy man')
		elif (number == 17):
			await message.channel.send('Psht, Psht')
		elif (number == 18):
			await message.channel.send('Exaaaaaactly')	
			
	if message.content.startswith('cbpic'): #Bot prints out one of 7 pictures (Can be any pictures)
		number = random.randint(0,6)
		if(number == 0):	
			await message.channel.send(file=discord.File('Insert photo file ID'))
		elif (number == 1):
			await message.channel.send(file=discord.File('Insert photo file ID'))
		elif (number == 2):
			await message.channel.send(file=discord.File('Insert photo file ID'))
		elif (number == 3):
			await message.channel.send(file=discord.File('Insert photo file ID'))
		elif (number == 4):
			await message.channel.send(file=discord.File('Insert photo file ID'))
		elif (number == 5):
			await message.channel.send(file=discord.File('Insert photo file ID'))
		elif (number == 6):
			await message.channel.send(file=discord.File('Insert photo file ID'))
			
	if message.content.startswith('cbcom'): #Bot compliments a person in the server with one of 5 compliments available
		number = random.randint(0,4)
		if(number == 0):
			await message.channel.send('<@Insert User ID> You thicc bro')
		elif (number == 1):
			await message.channel.send('<@Insert User ID> Here\'s a mint, because you got the Breath of the Wild')
		elif (number == 2):
			await message.channel.send('<@Insert User ID> You\'ll make a fine addition to my collection')
		elif (number == 3):
			await message.channel.send('<@Insert User ID> You make me go "Yeah Alright"')
		else:
			await message.channel.send('<@Insert User ID> You looking like a fresh flour tortilla')
			
	if message.content.startswith('cbhelp'): #Bot displays all available commands
		await message.channel.send('List of commands for Chris Bico Bot:\n-cbhello: Say hello!\n-cbbico: <Insert Emoji ID>\n-cb@: But where you at?\n-cbcp: Get a random catchphrase. Collect \'em all! (More will be added)\n-cbpic: Get a random photo of Chris Rico. Catch \'em all! (More will be added)\n-cbcom: Compliment Chris Rico!')
		
client.run('Insert Bot Token here')

