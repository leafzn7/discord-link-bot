import discord
import os
import re

TOKEN = os.getenv("DISCORD_TOKEN")

# Canal onde links serão apagados
CANAL_BLOQUEADO = 1522383551222251592

# Permissões necessárias para ler mensagens
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Detecta links
link_regex = re.compile(
    r"(https?://\S+|www\.\S+)",
    re.IGNORECASE
)

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")
    print(f"Protegendo o canal: {CANAL_BLOQUEADO}")

@client.event
async def on_message(message):

    # Ignora mensagens de bots
    if message.author.bot:
        return

    # Só verifica o canal escolhido
    if message.channel.id != CANAL_BLOQUEADO:
        return

    # Se tiver link, apaga
    if link_regex.search(message.content):
        try:
            await message.delete()
            print(f"Link apagado de {message.author}")

        except discord.Forbidden:
            print("ERRO: bot sem permissão para apagar mensagens.")

client.run(TOKEN)
