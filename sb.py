import discord

intents = discord.Intents.default()
intents.message_content = True

#bot = commands.Bot(command_prefix='$')

client = discord.Client(intents=intents)

companyList = {}

@client.event
async def on_ready():
    file = open(r"companyList.txt", "w+")

    
    
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name='with trees'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #companyList = {str : [start,end]}
    if message.content.startswith('Sustainability Bot where at?'):
        await message.channel.send('Hello!')


    #Check how good a specific company is
    elif message.content.startswith('$companyCheck'):
        # await message.channel.send('hi')
        #companyList.get()
        s = message.content.split()
        if (len(s) == 1):
            await message.channel.send("Please enter company : ")
            if message[1] == 'Shein':
                await message.channel.send("companyRating : 2/10")
                await message.channel.send(" - Uses Child labor")
                await message.channel.send(" - Terrible")
        elif(len(s) == 2):
            if s[1] == 'Shein':
                await message.channel.send("companyRating : 2/10")
                await message.channel.send(" - Uses Child labor")
                await message.channel.send(" - Terrible")
        else:
            await message.channel.send('Invalid Input')


client.run('MTAzODUxNTg4MDY1MDM1ODgxNA.Gi4HLB._vIK4V2mbt8Gbke3ClzyB8H9iTwZfXmS7eq8uU')


from discord.ext import commands

client = commands.Bot(command_prefix = '$')


# #client command
# @bot.command()
# async def CompanyCheck(ctx, arg):
#     await ctx.send(arg)