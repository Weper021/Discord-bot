import discord
from discord.ext import commands
import os
import openai
from dotenv import load_dotenv
from shop import StudyMealButton, FoodStreetButton

# 設定指令前綴和機器人 intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")


# 創建一個視圖，包含按鈕
class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None 

    @discord.ui.button(label="吃飯！", style=discord.ButtonStyle.primary)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        # 使用 interaction 來回應
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=f"吃學餐還是美食街" )

        more_buttons_view = MoreButtonsView()

        await interaction.response.edit_message(embed=embed,view=more_buttons_view)



class MoreButtonsView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="學餐", style=discord.ButtonStyle.secondary)
    async def option1(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=f"學餐" )

        study_meal_button=StudyMealButton()

        await interaction.response.send_message(embed=embed,view=study_meal_button)




    @discord.ui.button(label="美食街", style=discord.ButtonStyle.secondary)
    async def option2(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=f"美食街" )

        food_street=FoodStreetButton()

        await interaction.response.send_message(embed=embed,view=food_street)


    
async def load_cogs():
    await bot.load_extension('cogs.announcements')  # 加载公告功能
    await bot.load_extension('cogs.chat')
    await bot.load_extension('cogs.music')
# 将扩展加载到 bot 之前
@bot.event
async def on_ready():
    await load_cogs()  # 在 bot 准备好后加载 cogs
    print(f'Bot 已上线：{bot.user}')



# 當用戶輸入 !menu 時，顯示帶有按鈕的訊息
@bot.command()
async def menu(ctx):
    view = Menu()
    await ctx.reply( view=view)
    
async def chat(ctx, *, message: str):
    """與 GPT-4.0 進行對話"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    
    await ctx.send(response['choices'][0]['message']['content'])


bot.run(os.getenv("DISCORD_TOKEN"))