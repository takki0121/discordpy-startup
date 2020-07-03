from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

ID_ROLE_MEMBER = 728613284785422456

    @client.event
async def on_member_join(member):
    # 用意したIDから Role オブジェクトを取得
    role = member.guild.get_role(ID_ROLE_MEMBER)

    # 入ってきた Member に役職を付与
    await member.add_roles(role)
bot.run(token)
