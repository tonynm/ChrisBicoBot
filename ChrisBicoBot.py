import discord
from discord.ext import commands
import random
import datetime

random.seed()

description = "BicoBot is a bot modelled after a friend of mine"

helpText = """List of commands for Chris Bico Bot:\n-cbhello: Say hello!\n-cbbico: <:ChrisBico:662926031547662336>\n-cbat: But where you at?\n-cbcp: Get a random catchphrase. Collect \'em all! (More will be added)
-cbpic: Get a random photo of Chris Rico. Catch \'em all! (More will be added)\n-cbcom: Compliment Chris Rico!\n-cbdate: BicoBot tells us the day of the week!
-cbtomorrow: Bicobot tells us what day of week is tomorrow\n-cbeightball: Bicobot will act like a 8ball\n-cbbday: Celebrate someone\'s birthday! <:partying_face:751503332652089454>\n-cbbye: BicoBot says goodbye!"""

############## SECTION FOR ALL THE LISTS I WILL USE ##################
cpList = ['Shaking my head', 'Gotta do my dailies', 'Whatcha mean?', 'Pachinko Luck', 'Yeah, Yeah', 'What up. What up. What uuuuuup', 
'What the hell, man', 'Hey, that\'s pretty good!', 'Do it', 'Yeah, alright', 'Now hold on', 'China, china, china', 'Wait a minute', 'You trying to play sum Fornite?', 
'I forgot to watch Pawn Stars', 'Psht, Psht', 'Exaaaaaactly']

picList = ['ChrisPhoto.png', 'ChrisPhoto1.png', 'ChrisPhoto2.png', 'ChrisPhoto3.png', 'ChrisPhoto4.png', 'ChrisPhoto5.png',
'ChrisPhoto6.png', 'ChrisPhoto7.png', 'ChrisPhoto8.png', 'ChrisPhoto9.png', 'ChrisPhoto10.png', 'ChrisPhoto11.png', 'ChrisPhoto12.png']

comList = ['{} You thicc bro', '{} Here\'s a mint, because you got the Breath of the Wild', '{} You\'ll make a fine addition to my collection', 
'{} You make me go "Yeah Alright"', '{} All aboard the Bico Express *choo choo*', '{} You looking like a fresh flour tortilla']

dateList = ['{} is Monday', '{} is Tuesday', '{} is Wednesday', '{} is Thursday', '{} is Friday', '{} is Saturday', '{} is Sunday']

eightballList = ['As I see it, yes', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
"Don't count on it", 'It is certain', 'It is decidedly so', 'Most likely', 'My reply is no', 'My sources say no', 'Outlook not so good',
'Outlook good', 'Reply hazy, try again', 'Signs point to yes', 'Very doubtful', 'Without a doubt', 'Yes', 'Yes – definitely', 
'You may rely on it', 'POGGERS MY DOGGERS', 'Ask Tony']
######################################################################

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='cb', description=description, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready(): # When the bot successfully connects to the Discord Servers, this function is called
	print('We have logged in as {}'.format(bot.user.name))
	
@bot.event 
async def on_connect(): # Shows the status of the bot as "Playing cbhelp" 
	game = discord.Game('cbhelp')
	await bot.change_presence(activity=game)	
	
@bot.command() # Function for cbhello command. If used without directly mentioning someone, then just prints out Hello. Otherwise, prints out a Hello to the mentioned user
async def hello(ctx, user: discord.User=None):
	if not user:
		await ctx.channel.send("Hello")
	else:
		await ctx.channel.send("Hello {}".format(user.mention))
		
@bot.command() # Function that sends out the specified emoji if the emoji is available in the server
async def bico(ctx):
	await ctx.send("<:ChrisBico:662926031547662336>")
	
@bot.command() # Function that prints out a message at the predetermined user or the mentioned user if applicable
async def at(ctx, user: discord.User=None):
	if not user:
		await ctx.channel.send("<@209140413573890048> But where you at?")
	else:
		await ctx.channel.send("{} But where you at?".format(user.mention))
		
@bot.command() # Function that prints out a catchphrase based on the randomly generated number. Catchphrases are stored in a list called cpList
async def cp(ctx):
	number = random.randint(0, len(cpList)-1)
	await ctx.channel.send(cpList[number])
	
@bot.command() # Function that makes the bot post a picture in the server. Names of the picture files are stored in picList while the files are stored in the same directory as the ChrisBicoBot.py file
async def pic(ctx):
	number = random.randint(0,len(picList)-1)
	await ctx.channel.send(file=discord.File(picList[number]))
		
@bot.command() # Function that prints out a compliment phrase to either the predetermined user (the one with the Rico mention user id) or the mentioned user if applicable. Compliments messages are stored in comList.
async def com(ctx, user: discord.User=None):
	number = random.randint(0, len(comList)-1)
	ricoMention = '<@209140413573890048>'
	
	if not user:
		await ctx.channel.send(comList[number].format(ricoMention))
	else:
		await ctx.channel.send(comList[number].format(user.mention))

@bot.command() # Function that prints out a goodbye message to the mentioned user. There are three available goodbye messages.
async def bye(ctx, user: discord.User = None):
	number = random.randint(0,2)
	if(number == 0):
		await ctx.channel.send('{} Alright, Goodnight'.format(user.mention))
	elif (number == 1):
		await ctx.channel.send('{} Goodbye'.format(user.mention))
	elif (number == 2):
		await ctx.channel.send('{} Cya!'.format(user.mention))	
		
@bot.command() # Function that prints out the day of the week of today. 
async def date(ctx):
	day = datetime.datetime.today().weekday()
	await ctx.channel.send(dateList[day].format('Today'))
		
@bot.command() # Function that prints out the day of the week that is tomorrow.
async def tomorrow(ctx):
	day = datetime.datetime.today().weekday()
	if(day == 6):
		await ctx.channel.send(dateList[0].format('Tomorrow'))
	else:
		await ctx.channel.send(dateList[day+1].format('Tomorrow'))
		
@bot.command() # Function that gives the BicoBot a Magic Eightball type of feature. The magic eightball messages are stored in eightballList.
async def eightball(ctx):
	number = random.randint(0,len(eightballList)-1)
	await ctx.channel.send(eightballList[number])
		
@bot.command() # Function that lets the bot wish some a happy birthday. Either the predetermined user or a mentioned user if applicable.
async def bday(ctx, user: discord.User=None):
	if not user:
		await ctx.send("<@209140413573890048> <:ChrisBico:662926031547662336> Happy Birthday! <:partying_face:751503332652089454>")
	else:
		await ctx.send("<:partying_face:751503332652089454> Happy Birthday, {} <:partying_face:751503332652089454>!".format(user.mention))	
		
@bot.command() # Function that prints out a message with all the available commands and their functions.
async def help(ctx):
	await ctx.channel.send(helpText)
	

bot.run('Put Bot Token Here')

