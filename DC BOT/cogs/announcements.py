import discord  # 确保导入 discord
from discord.ext import commands
from discord.ui import View, Button
from utils.scraper import get_announcements

class AnnouncementView(View):
    def __init__(self, page=1):
        super().__init__()
        self.page = page
        self.announcements = get_announcements(self.page)

        for i, (title, link) in enumerate(self.announcements, start=1):
            button = Button(label=f"公告 {i}", style=discord.ButtonStyle.primary)
            button.callback = self.create_callback(link)
            self.add_item(button)

        next_page_button = Button(label="下一页", style=discord.ButtonStyle.secondary)
        next_page_button.callback = self.next_page
        self.add_item(next_page_button)

    def create_callback(self, link):
        async def callback(interaction):
            details = get_announcement_details(link)
            await interaction.response.send_message(f"公告详细内容：{details}")
        return callback

    async def next_page(self, interaction):
        self.page += 1
        self.announcements = get_announcements(self.page)
        await interaction.response.edit_message(view=self)

class Announcements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 文大公告(self, ctx):
        view = AnnouncementView()
        await ctx.send("这里是最新的文大公告:", view=view)

# 注册Cog
async def setup(bot):
    await bot.add_cog(Announcements(bot))  # 使用 await
