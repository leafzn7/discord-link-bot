import discord
import os
import re

TOKEN = os.getenv("DISCORD_TOKEN")

CANAL_BLOQUEADO = 1522383551222251592

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")
    print(f"Protegendo o canal: {CANAL_BLOQUEADO}")

@client.event
async def on_message(message):
    # Ignora mensagens enviadas por bots
    if message.author.bot:
        return

    # Só funciona no canal escolhido
    if message.channel.id != CANAL_BLOQUEADO:
        return

    # Encontrou link = apaga
    if link_regex.search(message.content):
        try:
            await message.delete()
            print(f"Link apagado de {message.author}")
        except discord.Forbidden:
            print("ERRO: O bot não tem permissão para apagar mensagens.")

client.run(TOKEN)
