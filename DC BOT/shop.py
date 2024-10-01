#shop.py

import discord

from menu import  restaurants_45, Grateful, HappyBreakfast, MOMOBreakfast, Pi_k , Longlong, Kitchen_3 , Vietnamese_Food, Don_Rice , Big_Q #45,感恩麵店,大家樂 ,
from menu import  U_Pin ,Big_Water_Fire ,Yummy_Rice ,Brother_Rice_Ball,Big_Red,Korean_Cuisine,Grandma_Sushi



from menu import CategoryMenu, SeaweedRiceRoll, Guguwaffle, SchoolBreakfast,Yuloong,JapaneseFood #貓喫一株,趙班長飯捲,咕咕鬆餅屋,娃子早餐,四海遊龍,村吉日料





#學餐
class StudyMealButton(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="貓喫一株", style=discord.ButtonStyle.primary)
    async def button_cat(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed = discord.Embed(
            title="貓喫一株",
            description="耶果/珍珠/仙草凍/冰淇凌 +10",
            color=discord.Color.random()
        )

        view = CategoryMenu()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

    @discord.ui.button(label="趙班長飯捲", style=discord.ButtonStyle.primary)
    async def button_Seaweed_rice_rol(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed = discord.Embed(
            title="趙班長飯捲",
            description="",
            color=discord.Color.random()
        )
        view = SeaweedRiceRoll()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

    @discord.ui.button(label="咕咕鬆餅屋", style=discord.ButtonStyle.primary)
    async def button_guguwaffle(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed = discord.Embed(
            title="咕咕鬆餅屋",
            description="""瓦芙(半圓)/鬆餅(圓)
            瓦芙/鬆餅+飲料 -5""",
            color=discord.Color.random()
        )

        view = Guguwaffle()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

    @discord.ui.button(label="娃子早餐", style=discord.ButtonStyle.primary)
    async def button_school_breakfast(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed = discord.Embed(
            title="娃子早餐",
            description="""""",
            color=discord.Color.random()
        )

        view = SchoolBreakfast()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

    @discord.ui.button(label="村吉日料", style=discord.ButtonStyle.primary)
    async def button_japanese_food(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed = discord.Embed(
            title="村吉日料",
            description="",
            color=discord.Color.random()
        )

        view = JapaneseFood()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view) 


    @discord.ui.button(label="四海遊龍", style=discord.ButtonStyle.primary)
    async def button_yuloong(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=discord.Color.random())
        embed = discord.Embed(
            title="四海遊龍",
            description="",
            color=discord.Color.random()
        )

        view = Yuloong()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)





#美食街
class FoodStreetButton(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="45(燉飯/義大利麵)", style=discord.ButtonStyle.primary)
    async def button_restaurants_45(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="45(燉飯/義大利麵)",
            description="a",
            color=discord.Color.random()
        )
        view = restaurants_45()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)


    @discord.ui.button(label="感恩麵店", style=discord.ButtonStyle.primary)
    async def button_Grateful(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="感恩麵店",
            description="a",
            color=discord.Color.random()
        )
        view = Grateful()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

    @discord.ui.button(label="大家樂早餐店", style=discord.ButtonStyle.primary)
    async def button_HappyBreakfast(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="大家樂早餐店",
            description="a",
            color=discord.Color.random()
        )
        view = HappyBreakfast()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)  

    @discord.ui.button(label="媽媽樂早餐店", style=discord.ButtonStyle.primary)
    async def button_MOMOBreakfast(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="媽媽樂早餐店",
            description="a",
            color=discord.Color.random()
        )
        view = MOMOBreakfast()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view) 


    @discord.ui.button(label="派克", style=discord.ButtonStyle.primary)
    async def button_Pi_k(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="派克",
            description="a",
            color=discord.Color.random()
        )
        view = Pi_k()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view) 


    @discord.ui.button(label="久久銅板美食", style=discord.ButtonStyle.primary)
    async def button_Longlong(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="久久銅板美食",
            description=""""飯、麺加大+10元														
""",
            color=discord.Color.random()
        )
        view = Longlong()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view) 


    @discord.ui.button(label="3號廚房", style=discord.ButtonStyle.primary)
    async def button_Kitchen_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="3號廚房",
            description=""""													
""",
            color=discord.Color.random()
        )
        view = Kitchen_3()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view) 


    @discord.ui.button(label="越南美食館", style=discord.ButtonStyle.primary)
    async def button_Vietnamese_Food(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="越南美食館",
            description=""""
加飯/麺/河粉/米粉	10	
加豬肉/雞肉	30
加牛肉/蝦/魚	50

""",
            color=discord.Color.random()
        )
        view = Vietnamese_Food()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view) 



        Don_Rice

    @discord.ui.button(label="有丼省錢", style=discord.ButtonStyle.primary)
    async def button_Don_Rice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="有丼省錢",
            description="""
""",
            color=discord.Color.random()
        )
        view = Don_Rice()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

        

    @discord.ui.button(label="大Q麵店", style=discord.ButtonStyle.primary)
    async def button_Big_Q(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="大Q麵店",
            description="""
""",
            color=discord.Color.random()
        )
        view = Big_Q()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)





    @discord.ui.button(label="御品軒", style=discord.ButtonStyle.primary)
    async def button_U_Pin(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="御品軒",
            description="""
""",
            color=discord.Color.random()
        )
        view = U_Pin()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)


    @discord.ui.button(label="𡘙/淼/焱", style=discord.ButtonStyle.primary)
    async def button_Big_Water_Fire(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="𡘙/淼/焱",
            description="""
""",
            color=discord.Color.random()
        )
        view = Big_Water_Fire()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

        
    @discord.ui.button(label="好吃炒飯", style=discord.ButtonStyle.primary)
    async def button_Yummy_Rice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="好吃炒飯",
            description="""
加飯+10 加荷包蛋+5
辣度  微辣 小辣 中辣 大辣
""",
            color=discord.Color.random()
        )
        view = Yummy_Rice()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

        

    @discord.ui.button(label="學長飯糰", style=discord.ButtonStyle.primary)
    async def button_Brother_Rice_Ball(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="學長飯糰",
            description="""
+蛋/起司/海苔 5 +飯不用錢
飯糰+飲料折5元
""",
            color=discord.Color.random()
        )
        view = Brother_Rice_Ball()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)




    @discord.ui.button(label="大紅袍", style=discord.ButtonStyle.primary)
    async def button_Big_Red(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="大紅袍",
            description="""麵加大加15元 加抄手加30元
""",
            color=discord.Color.random()
        )
        view = Big_Red()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)



    @discord.ui.button(label="景福館", style=discord.ButtonStyle.primary)
    async def button_Korean_Cuisine(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="景福館",
            description=""" 
""",
            color=discord.Color.random()
        )
        view = Korean_Cuisine()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)

    @discord.ui.button(label="阿婆壽司", style=discord.ButtonStyle.primary)
    async def button_Grandma_Sushi(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="阿婆壽司",
            description=""" 
""",
            color=discord.Color.random()
        )
        view = Grandma_Sushi()
        await interaction.response.send_message(content="請選擇一個菜單系列：",embed=embed, view=view)