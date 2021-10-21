from discord.ext import commands

client = commands.Bot(command_prefix='!')

participantes = ['Ane', 'Camila']

votoscamila = []
votosane = []

@client.event
async def on_ready():
    print('Iniciado')

@client.command()
async def bet(ctx, args1):
    if args1.lower() == 'camila':
        if f'{ctx.message.author.name}' in votosane:
            votosane.remove(str(ctx.message.author.name))
            votoscamila.append(str(ctx.author.name))
            await ctx.message.channel.send(f'`{ctx.message.author.name}` trocou o voto para *Camila*!')
            return

        if f'{ctx.message.author.name}' in votoscamila:
            await ctx.message.channel.send(f'`{ctx.message.author.name}` já apostou na *Camila*!')
            return

        votoscamila.append(str(ctx.author.name))
        await ctx.message.channel.send(f'`{ctx.message.author.name}` apostou na *Camila* com sucesso!')

    if args1.lower() == 'ane':
        if f'{ctx.message.author.name}' in votoscamila:
            votoscamila.remove(str(ctx.message.author.name))
            votosane.append(str(ctx.author.name))
            await ctx.message.channel.send(f'`{ctx.message.author.name}` trocou o voto para *Ane*!')
            return

        if f'{str(ctx.message.author.name)}' in votosane:
            await ctx.message.channel.send(f'`{ctx.message.author.name}` já apostou na *Ane*!')
            return

        votosane.append(str(ctx.author.name))
        await ctx.message.channel.send(f'`{ctx.message.author.name}` apostou na *Ane* com sucesso!')


@client.command()
async def placar(message):
    await message.channel.send(str('>                      **Participantes**     \n').center(50, ' '))
    for i in range(0, len(participantes)):
        await message.channel.send('> ***' + participantes[i] + '*** **:** \n')
        if i == 1:
            for c in range(0, len(votoscamila)):
                await message.channel.send('>          **' + votoscamila[c] + '**')
        if i == 0:
            for a in range(0, len(votosane)):
                await message.channel.send('>          **' + votosane[a] + '**')

@client.command()
async def limpar(ctx):
    if f'{ctx.message.author.name}' in votoscamila:
        votoscamila.remove(str(ctx.message.author.name))
        await ctx.message.channel.send(f'`{ctx.message.author.name}` teve o voto removido da participante *Camila*!')
    if f'{ctx.message.author.name}' in votosane:
        votosane.remove(str(ctx.message.author.name))
        await ctx.message.channel.send(f'`{ctx.message.author.name}` teve o voto removido da participante *Ane*!')
    else:
        await ctx.message.channel.send(f'`{ctx.message.author.name}` não votou em nenhuma participante ainda!')

client.run('Secret')
