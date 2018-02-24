import discord
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from redbot.core.data_manager import bundled_data_path
import io
from PIL import Image



class Reee:

    def __init__(self, bot):
        self.bot = bot
        self.increment = 2
        self.start_size = (1024, 1024)
        self.smallest = (32, 32)
        self.config = Config.get_conf(self, 1545234853)
        default_guild = {"zio":False, "reee":False, "tank":False}
        self.config.register_guild(**default_guild)
    
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild.id == "236313384100954113" and message.channel.id not in ["244653444504223755", "367879950466023425"]:
            return
        msg = message.content.lower()
        guild = message.guild

        if "reee" in msg and await self.config.guild(guild).reee():
            for word in msg.split(" "):
                if "reee" in word:
                    file = await self.change_size_reee(len(word)-3)
                    await message.channel.send(file=file)
        if "zioo" in msg and await self.config.guild(guild).zio():
            for word in msg.split(" "):
                if "zioo" in word:
                    file = await self.change_size_zio(len(word)-3)
                    await message.channel.send(file=file)
        if "taaa" in msg and "nk" in msg and await self.config.guild(guild).tank():
            for word in msg.split(" "):
                if "taaa" in word:
                    file = await self.change_size_tank(len(word)-3)
                    await message.channel.send(file=file)
            
    async def change_size_reee(self, size):
        length, width = self.smallest
        im = Image.open(str(bundled_data_path(self)) + "/reee.png")
        im.thumbnail((length*size, width*size), Image.ANTIALIAS)
        # im.save("data/reee/newreee.png")
        byte_array = io.BytesIO()
        im.save(byte_array, format="PNG")
        return discord.File(byte_array.getvalue(), filename="reeee.png")

    async def change_size_zio(self, size):
        length, width = self.smallest
        im = Image.open(str(bundled_data_path(self)) + "/zio.jpg")
        im.thumbnail((length*size, width*size), Image.ANTIALIAS)
        byte_array = io.BytesIO()
        im.save(byte_array, format="PNG")
        return discord.File(byte_array.getvalue(), filename="zio.png")

    async def change_size_tank(self, size):
        length, width = self.smallest
        im = Image.open(str(bundled_data_path(self)) + "/tank.png")
        im.thumbnail((length*size, width*size), Image.ANTIALIAS)
        byte_array = io.BytesIO()
        im.save(byte_array, format="PNG")
        return discord.File(byte_array.getvalue(), filename="tank.png")

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def setreee(self, ctx):
        """Posts various sized reee's when reee is posted"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).reee():
            await self.config.guild(guild).reee.set(True)
            await ctx.send("I will post REEE images on this guild now.")
        else:
            await self.config.guild(guild).reee.set(False)
            await ctx.send("I will not post REEE images on this guild now.")

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def setzio(self, ctx):
        """Posts various sized zio's when zioo isposted"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).zio():
            await self.config.guild(guild).zio.set(True)
            await ctx.send("I will post zio images on this guild now.")
        else:
            await self.config.guild(guild).zio.set(False)
            await ctx.send("I will not post zio images on this guild now.")

    @commands.command(pass_context=True)
    @checks.mod_or_permissions(manage_channels=True)
    async def settank(self, ctx):
        """Posts various sized tanks when taaank is posted"""
        guild = ctx.message.guild
        if not await self.config.guild(guild).tank():
            await self.config.guild(guild).tank.set(True)
            await ctx.send("I will post tank images on this guild now.")
        else:
            await self.config.guild(guild).tank.set(False)
            await ctx.send("I will not post tank images on this guild now.")
