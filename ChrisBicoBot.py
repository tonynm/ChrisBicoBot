import discord
from discord.ext import commands
import random
import datetime

random.seed()

description = "BicoBot is a bot modelled after a friend of mine"
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='cb', description=description, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
	print('We have logged in as {}'.format(bot.user.name))
	
@bot.event 
async def on_connect():
	game = discord.Game('cbhelp')
	await bot.change_presence(activity=game)	
	
@bot.command()
async def hello(ctx, user: discord.User=None):
	if not user:
		await ctx.channel.send("Hello")
	else:
		await ctx.channel.send("Hello {}".format(user.mention))
		
@bot.command()
async def bico(ctx):
	await ctx.send("<:ChrisBico:662926031547662336>")
	
@bot.command()
async def at(ctx, user: discord.User=None):
	if not user:
		await ctx.channel.send("<@209140413573890048> But where you at?")
	else:
		await ctx.channel.send("{} But where you at?".format(user.mention))
		
@bot.command()
async def cp(ctx):
	number = random.randint(0, 19)
	if (number == 0):
		await ctx.channel.send('Shaking my head')
	elif (number == 1):
		await ctx.channel.send('Gotta do my dailies')
	elif (number == 2):
		await ctx.channel.send('Whatcha mean?')
	elif (number == 3):
		await ctx.channel.send('Pachinko Luck')
	elif (number == 4):
		await ctx.channel.send('Yeah, Yeah')
	elif (number == 5):
		await ctx.channel.send('The Fuck?')
	elif (number == 6):
		await ctx.channel.send('What up. What up. What uuuuuup')
	elif (number == 7):
		await ctx.channel.send('What the hell, man')
	elif (number == 8):
		await ctx.channel.send('Hey, that\'s pretty good!')
	elif (number == 9):
		await ctx.channel.send('Do it')
	elif (number == 10):
		await ctx.channel.send('Yeah, alright')
	elif (number == 11):
		await ctx.channel.send('Now hold on')
	elif (number == 12):
		await ctx.channel.send('China, china, china')
	elif (number == 13):
		await ctx.channel.send('Wait a minute')
	elif (number == 14):
		await ctx.channel.send('You trying to play sum Fornite?')
	elif (number == 15):
		await ctx.channel.send('I forgot to watch Pawn Stars')
	elif (number == 16):
		await ctx.channel.send('You stupid bitch')
	elif (number == 17):
		await ctx.channel.send('Psht, Psht')
	elif (number == 18):
		await ctx.channel.send('Exaaaaaactly')
	elif (number == 19):
		await ctx.channel.send('Eat ***ASS***')
		
@bot.command()
async def pic(ctx):
	number = random.randint(0,12)
	if(number == 0):
		await ctx.channel.send(file=discord.File('ChrisPhoto.png'))
	elif (number == 1):
		await ctx.channel.send(file=discord.File('ChrisPhoto1.png'))
	elif (number == 2):
		await ctx.channel.send(file=discord.File('ChrisPhoto2.png'))
	elif (number == 3):
		await ctx.channel.send(file=discord.File('ChrisPhoto3.png'))
	elif (number == 4):
		await ctx.channel.send(file=discord.File('ChrisPhoto4.png'))
	elif (number == 5):
		await ctx.channel.send(file=discord.File('ChrisPhoto5.png'))
	elif (number == 6):
		await ctx.channel.send(file=discord.File('ChrisPhoto6.png'))
	elif (number == 7):
		await ctx.channel.send(file=discord.File('ChrisPhoto7.png'))
	elif (number == 8):
		await ctx.channel.send(file=discord.File('ChrisPhoto8.png'))
	elif (number == 9):
		await ctx.channel.send(file=discord.File('ChrisPhoto9.png'))
	elif (number == 10):
		await ctx.channel.send(file=discord.File('ChrisPhoto10.png'))
	elif (number == 11):
		await ctx.channel.send(file=discord.File('ChrisPhoto11.png'))
	elif (number == 12):
		await ctx.channel.send(file=discord.File('ChrisPhoto12.png'))
@bot.command()
async def com(ctx, user: discord.User=None):
	if not user:
		number = random.randint(0,5)
		if(number == 0):
			await ctx.channel.send('<@209140413573890048> You thicc bro')
		elif (number == 1):
			await ctx.channel.send('<@209140413573890048> Here\'s a mint, because you got the Breath of the Wild')
		elif (number == 2):
			await ctx.channel.send('<@209140413573890048> You\'ll make a fine addition to my collection')
		elif (number == 3):
			await ctx.channel.send('<@209140413573890048> You make me go "Yeah Alright"')
		elif (number == 4):
			await ctx.channel.send('<@209140413573890048> All aboard the Bico Express *choo choo*')	
		else:
			await ctx.channel.send('<@209140413573890048> You looking like a fresh flour tortilla')
	else:
		number = random.randint(0,5)
		if(number == 0):
			await ctx.channel.send('{} You thicc bro'.format(user.mention))
		elif(number == 1):
			await ctx.channel.send('{} Here\'s a mint, because you got the Breath of the Wild'.format(user.mention))
		elif(number == 2):
			await ctx.channel.send('{} You\'ll make a fine addition to my collection'.format(user.mention))
		elif(number == 3):
			await ctx.channel.send('{} You make me go "Yeah Alright"'.format(user.mention))
		elif(number == 4):
			await ctx.channel.send('{} All aboard the Bico Express *choo choo*'.format(user.mention))
		else:
			await ctx.channel.send('{} You looking like a fresh flour tortilla'.format(user.mention))


@bot.command()
async def bye(ctx, user: discord.User = None):
	number = random.randint(0,2)
	if(number == 0):
		await ctx.channel.send('{} Alright, Goodnight'.format(user.mention))
	elif (number == 1):
		await ctx.channel.send('{} Goodbye'.format(user.mention))
	elif (number == 2):
		await ctx.channel.send('{} Cya!'.format(user.mention))	
		
@bot.command()
async def date(ctx):
	day = datetime.datetime.today().weekday()
	if(day == 0):
		await ctx.channel.send('Today is Monday')
	elif(day == 1):
		await ctx.channel.send('Today is Tuesday')
	elif(day == 2):
		await ctx.channel.send('Today is Wednesday')
	elif(day == 3):
		await ctx.channel.send('Today is Thursday')
	elif(day == 4):
		await ctx.channel.send('Today is Friday')
	elif(day == 5):
		await ctx.channel.send('Today is Saturday')
	elif(day == 6):
		await ctx.channel.send('Today is Sunday')
		
@bot.command()
async def tomorrow(ctx):
	day = datetime.datetime.today().weekday()
	if(day == 0):
		await ctx.channel.send('Tomorrow is Tuesday')
	elif(day == 1):
		await ctx.channel.send('Tomorrow is Wednesday')
	elif(day == 2):
		await ctx.channel.send('Tomorrow is Thursday')
	elif(day == 3):
		await ctx.channel.send('Tomorrow is Friday')
	elif(day == 4):
		await ctx.channel.send('Tomorrow is Saturday')
	elif(day == 5):
		await ctx.channel.send('Tomorrow is Sunday')
	elif(day == 6):
		await ctx.channel.send('Tomorrow is Monday')	
		
@bot.command()
async def eightball(ctx):
	number = random.randint(0,21)
	if(number == 0):
		await ctx.channel.send('As I see it, yes')
	elif(number == 1):
		await ctx.channel.send('Ask again later')
	elif(number == 2):
		await ctx.channel.send('Better not tell you now')
	elif(number == 3):
		await ctx.channel.send('Cannot predict now')
	elif(number == 4):
		await ctx.channel.send('Concentrate and ask again')
	elif(number == 5):
		await ctx.channel.send("Don't count on it")
	elif(number == 6):
		await ctx.channel.send('It is certain')
	elif(number == 7):
		await ctx.channel.send('It is decidedly so')
	elif(number == 8):
		await ctx.channel.send('Most likely')
	elif(number == 9):
		await ctx.channel.send('My reply is no')
	elif(number == 10):
		await ctx.channel.send('My sources say no')
	elif(number == 11):
		await ctx.channel.send('Outlook not so good')
	elif(number == 12):
		await ctx.channel.send('Outlook good')
	elif(number == 13):
		await ctx.channel.send('Reply hazy, try again')
	elif(number == 14):
		await ctx.channel.send('Signs point to yes')
	elif(number == 15):
		await ctx.channel.send('Very doubtful')
	elif(number == 16):
		await ctx.channel.send('Without a doubt')
	elif(number == 17):
		await ctx.channel.send('Yes')
	elif(number == 18):
		await ctx.channel.send('Yes – definitely')
	elif(number == 19):
		await ctx.channel.send('You may rely on it')
	elif(number == 20):
		await ctx.channel.send('POGGERS MY DOGGERS')
	elif(number == 21):
		await ctx.channel.send('Ask Tony')
		
@bot.command()
async def bday(ctx, user: discord.User=None):
	if not user:
		await ctx.send("<@209140413573890048> <:ChrisBico:662926031547662336> Happy Birthday! <:partying_face:751503332652089454>")
	else:
		await ctx.send("<:partying_face:751503332652089454> Happy Birthday, {} <:partying_face:751503332652089454>!".format(user.mention))	
		
@bot.command()
async def help(ctx):
	await ctx.channel.send('List of commands for Chris Bico Bot:\n-cbhello: Say hello!\n-cbbico: <:ChrisBico:662926031547662336>\n-cbat: But where you at?\n-cbcp: Get a random catchphrase. Collect \'em all! (More will be added)\n-cbpic: Get a random photo of Chris Rico. Catch \'em all! (More will be added)\n-cbcom: Compliment Chris Rico!\n-cbdate: BicoBot tells us the day of the week!\n-cbtomorrow: Bicobot tells us what day of week is tomorrow\n-cbeightball: Bicobot will act like a 8ball\n-cbbday: Celebrate someone\'s birthday! <:partying_face:751503332652089454>\n-cbbye: BicoBot says goodbye!')		
	

bot.run('Put Bot Token Here')

