from discord


client = commands.Bot(description = "a", command_prefix = ".", self_bot = True)

client.remove_command('help')

@client.event
async def on_ready():
   user = await client.fetch_user("[BAK] Glogwa68 WATTATATATATA#0007")
print(user)

client.run('MzYwNTAwNjU5NzgwNTgzNDI0.YY7GSQ.V25bNfeMBqXcVpLFgp25r5YhOWE')