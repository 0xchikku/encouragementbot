import discord

client = discord.Client()

@client.event
async def on_ready():
	print('Lets Go!')

client.run('ODUwNjI2NjY3MzU2NDg3Njgw.YLsd0Q.ZKBFcH3P-ArLuwqwah1augvVOqk')