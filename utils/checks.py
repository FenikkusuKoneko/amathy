from discord.ext import commands
import os
from shutil import copyfile
import discord


def check_folder(path):
    if os.path.exists(path):
        return True
    return False


def check_create_folder(path):
    if not check_folder(path):
        print(f"[Action] I'm creating a folder for you... ({path})")
        os.makedirs(path)


def check_file(path):
    if os.path.isfile(path):
        return True
    return False


def check_copy_file(path):
    if not check_file(path):
        print(f"[Action] I'm copying a base file for you... ({path}). \nYou have to manually edit something in it!")
        source_path = path.split("/")[-1]
        copyfile(f"utils/base/{source_path}", path)


def check_create_file(path, content):
    if not check_file(path):
        print(f"[Action] I'm creating a file for you... ({path})")
        with open(path, "w") as f:
            f.write(content)


def is_creator():
    async def is_creator_check(ctx):
        uid = ctx.message.author.id
        if uid in ctx.bot.owner_ids:
            return True
        else:
            await ctx.send("Creator only access!")
            return False
    return commands.check(is_creator_check)


def is_guild_admin():
    async def inside_check(ctx):
        u = ctx.message.author
        if u.guild_permissions.administrator:
            return True
        await ctx.send("No access! You need to be a server administrator to run this command.")
        return False
    return commands.check(inside_check)


def is_nsfw():
    async def inside_check(ctx):
        if ctx.channel.is_nsfw():
            return True
        desc = "NSFW commands can only be used in NSFW marked channels."
        emb = discord.Embed(title="You can't use this here!", description=desc)
        emb.set_image(url="https://i.imgur.com/oe4iK5i.gif")
        await ctx.send(embed=emb)
        return False
    return commands.check(inside_check)