import discord
import asyncio
import aiohttp
from discord.ext import commands
from redbot.core import checks, Config
from datetime import datetime
import logging


class Unity4J:

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 458467658435)
        default_global = {"last_sent":0}
        self.config.register_global(**default_global)
        self.loop = bot.loop.create_task(self.message_need_a_role())

    async def get_role(self, guild, role_id):
        need_a_role = None
        for role in guild.roles:
            if role.id == role_id:
                need_a_role = role
        return need_a_role

    @commands.command()
    async def unity4jroles(self, ctx):
        guild = ctx.message. guild
        if guild.id not in [469771424274317312, 321105104931389440]:
            return
        em = discord.Embed()
        em.description = "Type only the command after the role to be assigned that role:\n<#469906777509462016> <@&469906844157214721> `;analytics`\n<#470636037341708308> <@&470398819763355659> `;blogger`\n<#471263120338321421> <@&471145950522376202> `;design`\n<#469782575225896961> <@&469805682204606464> `;facebooker`\n<#473234759254802432> <@&473220172958793760> `;faith`\n<#470735149395607572> <@&470735200540688394> `;gabber`\n<#470725079865491468> <@&470724785480007680> `;google`\n<#470997152584171520> <@&469809793947795466> `;graphics`\n<#470387099640659978> <@&470397209733496863> `;instagrammer`\n<#471103818826776576> <@&471107903777144852> `;legal`\n<#471146260405944321> <@&471146076573925377> `;minds`\n<#469807830250160128> <@&469809734141345793> `;music`\n<#469808195905519642> <@&470393412688805888> `;podcaster`\n<#471009013564440576> <@&471062064010493953> `;proofreader`\n<#469782594901377025> <@&469806187462787074> `;redditor`\n<#470390787566469150> <@&470390853492408340> `;researcher`\n<#469807930104086540> <@&469885340006613003> `;scribe`\n<#469825488664395788> <@&469825196681854978> `;translator`\n<#469782615864377345> <@&469806854881673227> `;steemian`\n<#469807930104086540> <@&471232671784239104> `;streamteam`\n<#472882645894955010> <@&472987153857642496> `;truth`\n<#470638042428997643> <@&470638081909850113> `;tumblr`\n<#469782554682064905> <@&469806127832629259> `;tweeter`\n<#469807723320442890> <@&469809330489655296> `;video`\n<#470549754145800200> <@&469809460962000896> `;webteam`\n<#470388961517502474> <@&470390921293463582> `;youtuber`\n"
        em.set_thumbnail(url=guild.icon_url)
        em.set_author(name="{} Self Assignable Roles".format(guild.name), icon_url=guild.icon_url)
        em.timestamp = datetime.utcnow()
        await ctx.send(embed=em)



    async def message_need_a_role(self):
        await self.bot.wait_until_ready()
        while self is self.bot.get_cog("Unity4J"):
            last_checked = datetime.utcfromtimestamp(await self.config.last_sent())
            now = datetime.utcnow()
            if last_checked.day != now.day:
                guild = self.bot.get_guild(469771424274317312)
                role = await self.get_role(guild, 470518033840865290)# get the need_a_role role object
                for member in role.members:
                    try:
                        await member.send("Hey there. You have no role assigned yet and we want to help you settle into your #Unity4J team as soon as possible. Please go to #role, read through the role descriptions and answer the questions, and to <#469816208464805896> or <#470402195477626910> if you need any help. Thank you!")
                    except Exception as e:
                        print("{}({}): {}".format(member.name, member.id, e))
                await self.config.last_sent.set(now.timestamp())
            await asyncio.sleep(600)


    async def on_member_update(self, before, after):
        guild = before.guild
        if guild.id != 469771424274317312:
            return
        before_role_id = [role.id for role in before.roles]
        after_role_id = [role.id for role in after.roles]
        if 470458449839259649 in after_role_id and 470458449839259649 not in before_role_id:
            try:
                await after.send("Congratulations {}, you have earned the 'Helpful' role for being kind and helpful to your fellow members of the movement! Thank you for being such a wonderful human being and helping to save Julian!".format(after.mention))
            except Exception as e:
                print(e)
        if 470898257774641153 in after_role_id and 470898257774641153 not in before_role_id:
            try:
                await after.send("Congratulations {}, you have earned the 'Contributing' role for contributing to work being utilised by the movement! Thank you for your efforts to help save Julian!".format(after.mention))
            except Exception as e:
                print(e)
        
    async def on_message(self, message):
        if message.channel.id == 469783041145962496 or message.channel.id == 469771424773701649:
            if "donate" in message.content.lower() and not message.author.bot:
                await message.channel.send("Would you like to donate to support Julian? Please do so at https://iamwikileaks.org/donate and https://justice4assange.com. Thank you so much for supporting him!")
                return
        

