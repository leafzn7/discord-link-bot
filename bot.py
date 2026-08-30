import os
import re
import discord

# =========================
# CONFIGURAÇÕES
# =========================

TOKEN = os.getenv("DISCORD_TOKEN")

# Canal onde links serão apagados
CANAL_BLOQUEADO = 1522383551222251592

# Detecta:
# https://site.com
# http://site.com
# www.site.com
# site.com
# discord.gg/xxxx
LINK_REGEX = re.compile(
    r"(?:https?://\S+|www\.\S+|discord\.gg/\S+|"
    r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/\S*)?)",
    re.IGNORECASE,
)

# =========================
# INTENTS
# =========================

intents = discord.Intents.default()

# NECESSÁRIO para o bot conseguir ler o texto das mensagens
intents.message_content = True

client = discord.Client(intents=intents)


# =========================
# BOT ONLINE
# =========================

@client.event
async def on_ready():
    print("=" * 40)
    print(f"BOT ONLINE: {client.user}")
    print(f"ID DO BOT: {client.user.id}")
    print(f"CANAL PROTEGIDO: {CANAL_BLOQUEADO}")
    print("=" * 40)


# =========================
# BLOQUEIO DE LINKS
# =========================

@client.event
async def on_message(message):

    # Ignora mensagens do próprio bot e de outros bots
    if message.author.bot:
        return

    # Só funciona no canal escolhido
    if message.channel.id != CANAL_BLOQUEADO:
        return

    # Procura link na mensagem
    if LINK_REGEX.search(message.content):

        try:
            await message.delete()

            print(
                f"Link apagado | "
                f"Usuário: {message.author} | "
                f"Canal: {message.channel.id}"
            )

        except discord.Forbidden:
            print(
                "ERRO: O bot não tem permissão "
                "para Gerenciar Mensagens."
            )

        except discord.HTTPException as erro:
            print(f"Erro ao apagar mensagem: {erro}")


# =========================
# INICIAR
# =========================

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN não foi encontrado nas Variables do Railway."
    )

client.run(TOKEN)
