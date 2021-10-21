from discord.ext import commands

client = commands.Bot(command_prefix='!')

votoscamila = []
votosane = []

@client.event
async def on_ready():
    print('Iniciado como {}'.format(client.user))

@client.command()
async def bet(ctx, args1):
    if args1.lower() == 'camila':
        if f'<@{str(ctx.message.author.id)}>' in votosane:
            votosane.remove(f'<@{str(ctx.message.author.id)}>')
            votoscamila.append(f'<@{str(ctx.message.author.id)}>')
            await ctx.message.channel.send(f'<@{ctx.message.author.id}> trocou o voto para **Camila**!')
            return

        if f'<@{str(ctx.message.author.id)}>' in votoscamila:
            await ctx.message.channel.send(f'<@{ctx.message.author.id}> já apostou na **Camila**!')
            return

        votoscamila.append(f'<@{str(ctx.message.author.id)}>')
        await ctx.message.channel.send(f'<@{ctx.message.author.id}> apostou na **Camila** com sucesso!')

    if args1.lower() == 'ane':
        if f'<@{str(ctx.message.author.id)}>' in votoscamila:
            votoscamila.remove(f'<@{str(ctx.message.author.id)}>')
            votosane.append(f'<@{str(ctx.message.author.id)}>')
            await ctx.message.channel.send(f'<@{ctx.message.author.id}> trocou o voto para **Ane**!')
            return

        if f'<@{str(ctx.message.author.id)}>' in votosane:
            await ctx.message.channel.send(f'<@{ctx.message.author.id}> já apostou na **Ane**!')
            return

        votosane.append(f'<@{str(ctx.message.author.id)}>')
        await ctx.message.channel.send(f'<@{ctx.message.author.id}> apostou na **Ane** com sucesso!')


@client.command()
async def placar(message):
    await message.channel.send(str('>>>                            **Participantes**\n'
                                   '**Camila : **\n'
                                   + '\n'.join(votoscamila)) +
                                   '\n **Ane :** \n'
                                   + '\n'.join(votosane))

@client.command()
async def retirar(ctx):
    if f'<@{str(ctx.message.author.id)}>' in votoscamila:
        votoscamila.remove(f'<@{str(ctx.message.author.id)}>')
        await ctx.message.channel.send(f'<@{ctx.message.author.id}> teve o voto removido da participante **Camila**!')
        return
    if f'<@{str(ctx.message.author.id)}>' in votosane:
        votosane.remove(f'<@{str(ctx.message.author.id)}>')
        await ctx.message.channel.send(f'<@{ctx.message.author.id}> teve o voto removido da participante **Ane**!')
        return
    await ctx.message.channel.send(f'<@{ctx.message.author.id}> não votou em nenhuma participante ainda!')

@client.command()
async def resetar(ctx):
    await ctx.message.channel.send('Os votos foram resetados!')
    votoscamila.clear()
    votosane.clear()

@client.command()
async def vitoria(ctx, *, args1):
    if len(votoscamila) == 0 and len(votosane) == 0:
        await ctx.message.channel.send('Nenhum voto encontrado!')
        return
    if args1.lower() == 'camila':
        await ctx.message.channel.send(str('>>>                            **Vitória da Camila**\n'
                                       '**Pessoas que acreditaram no potencial dela : **\n'
                                       + '\n'.join(votoscamila)))
        votoscamila.clear()
        votosane.clear()
    if args1.lower() == 'ane':
        await ctx.message.channel.send(str('>>>                            **Vitória da Ane**\n'
                                       '**Pessoas que acreditaram no potencial dela : **\n'
                                       + '\n'.join(votosane)))
        votoscamila.clear()
        votosane.clear()

client.run('SECRET')
