#menu.py
import discord
from discord import Embed, Interaction, ButtonStyle
from discord.ui import View, Button

#貓喫一株
class CategoryMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    #告知更新時間
    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2022/3/24")
        return embed

    @discord.ui.button(label="奶蓋系列", style=discord.ButtonStyle.secondary)
    async def button_naigai(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="奶蓋系列",
            color=discord.Color.random()
        )
        embed.add_field(name="奶蓋茉香綠茶", value="55", inline=True)
        embed.add_field(name="奶蓋蜜香紅茶", value="55", inline=True)
        embed.add_field(name="奶蓋四季春", value="55", inline=True)
        embed.add_field(name="奶蓋烏龍綠", value="55", inline=True)
        embed.add_field(name="抹茶奶蓋綠茶", value="65", inline=True)
        embed.add_field(name="奶蓋可可亞", value="65", inline=True)

        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


    @discord.ui.button(label="純濃鮮奶系列", style=discord.ButtonStyle.secondary)
    async def button_pure_milk(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="純濃鮮奶系列",
            color=discord.Color.random()
        )
        embed.add_field(name="純濃鮮奶茶", value="M:40 L:50", inline=True)
        embed.add_field(name="榛果鮮奶茶", value="M:45 L:55", inline=True)
        embed.add_field(name="可可鮮奶茶", value="M:45 L:55", inline=True)
        embed.add_field(name="抹茶鮮奶茶", value="M:45 L:60", inline=True)
        embed.add_field(name="黑糖珍珠鮮奶茶", value="M:50 L:60", inline=True)
        embed = self.add_footer(embed)
    
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label="特調系列", style=discord.ButtonStyle.secondary)
    async def button_special_mix(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="特調系列",
            color=discord.Color.random()
        )
        embed.add_field(name="梅子綠茶", value="45", inline=True)
        embed.add_field(name="蜂蜜紅/綠茶", value="50", inline=True)
        embed.add_field(name="蜂蜜烏龍茶", value="50", inline=True)
        embed.add_field(name="蜂蜜檸檬", value="50", inline=True)
        embed.add_field(name="金桔檸檬", value="55", inline=True)
        embed.add_field(name="甘蔗檸檬", value="50", inline=True)
        embed.add_field(name="甘蔗青茶", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="冬瓜系列", style=discord.ButtonStyle.secondary)
    async def button_winter_melon(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="冬瓜系列",
            color=discord.Color.random()
        )
        embed.add_field(name="冬瓜茶", value="30", inline=True)
        embed.add_field(name="冬瓜青茶", value="30", inline=True)
        embed.add_field(name="冬瓜仙草蜜", value="40", inline=True)
        embed.add_field(name="冬瓜檸檬", value="45", inline=True)
        embed.add_field(name="冬瓜鮮奶", value="50", inline=True)
        embed = self.add_footer(embed)

        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="喫茶茗品系列", style=discord.ButtonStyle.secondary)
    async def button_tea(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="喫茶茗品系列",
            color=discord.Color.random()
        )
        embed.add_field(name="錫蘭紅茶", value="30", inline=True)
        embed.add_field(name="特級紅茶", value="30", inline=True)
        embed.add_field(name="茉香綠茶", value="30", inline=True)
        embed.add_field(name="烏龍綠茶", value="30", inline=True)
        embed.add_field(name="高山綠茶", value="30", inline=True)
        embed.add_field(name="四季春茶", value="30", inline=True)
        embed = self.add_footer(embed)      
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="茶奶系列", style=discord.ButtonStyle.secondary)
    async def button_tea_milk(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="茶奶系列",
            color=discord.Color.random()
        )
        embed.add_field(name="特級奶綠", value="M:40 L:50", inline=True)
        embed.add_field(name="椰果奶茶", value="M:40 L:50", inline=True)
        embed.add_field(name="珍珠奶茶", value="M:40 L:50", inline=True)
        embed.add_field(name="仙草凍奶茶", value="M:40 L:50", inline=True)
        embed.add_field(name="烏龍奶茶", value="M:40 L:50", inline=True)
        embed = self.add_footer(embed)      
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="鮮果系列", style=discord.ButtonStyle.secondary)
    async def button_fresh_fruit(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="鮮果系列",
            color=discord.Color.random()
        )
        embed.add_field(name="柳橙綠茶", value="65", inline=True)
        embed.add_field(name="葡萄柚綠茶", value="70", inline=True)
        embed.add_field(name="百香綠茶", value="65", inline=True)
        embed = self.add_footer(embed)      
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="冰淇淋系列", style=discord.ButtonStyle.secondary)
    async def button_ice_cream(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="冰淇淋系列",
            color=discord.Color.random()
        )
        embed.add_field(name="冰淇淋紅茶", value="50", inline=True)
        embed.add_field(name="冰淇淋鮮奶茶", value="65", inline=True)
        embed = self.add_footer(embed)      
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="多多系列", style=discord.ButtonStyle.secondary)
    async def button_duoduo(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="多多系列",
            color=discord.Color.random()
        )
        embed.add_field(name="多多綠茶", value="40", inline=True)
        embed.add_field(name="多多檸檬", value="50", inline=True)
        embed.add_field(name="多多葡萄柚", value="70", inline=True)
        embed = self.add_footer(embed)      
        await interaction.response.edit_message(embed=embed)




class restaurants_45(discord.ui.View):
    def __init__(self):
        super().__init__()

    # Utility function to add footer to embeds
    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="白雪公主系列", style=discord.ButtonStyle.secondary)
    async def button_snow_white(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="白雪公主系列",
            color=discord.Color.random()
        )
        embed.add_field(name="A1 奶油辣椒義大利麵", value="125", inline=True)
        embed.add_field(name="A2 唐揚野菇奶油白醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="A3 起司培根奶油白醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="A4 起司燻雞奶油白醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="A5 日式炸雞腿塊佐奶油白醬(燉飯/義大利麵)", value="155", inline=True)
        embed.add_field(name="A6 日式炸豬排佐奶油白醬(燉飯/義大利麵)", value="160", inline=True)
        embed.add_field(name="A7 蒜香蛤蜊佐奶油白醬(燉飯/義大利麵)", value="175", inline=True)
        embed.add_field(name="A8 海鮮總匯佐奶油白醬(燉飯/義大利麵)", value="180", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="綠野仙蹤系列", style=discord.ButtonStyle.secondary)
    async def button_green_forest(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="綠野仙蹤系列",
            color=discord.Color.random()
        )
        embed.add_field(name="B1 乳酪青醬(燉飯/義大利麵)", value="125", inline=True)
        embed.add_field(name="B2 唐揚野菇青醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="B3 起司培根青醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="B4 起司燻雞青醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="B5 日式炸雞腿塊佐青醬(燉飯/義大利麵)", value="155", inline=True)
        embed.add_field(name="B6 日式炸豬排佐青醬(燉飯/義大利麵)", value="160", inline=True)
        embed.add_field(name="B7 蒜香蛤蜊佐青醬(燉飯/義大利麵)", value="175", inline=True)
        embed.add_field(name="B8 海鮮總匯佐青醬(燉飯/義大利麵)", value="180", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="天鵝絨系列", style=discord.ButtonStyle.secondary)
    async def button_velvet(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="天鵝絨系列",
            color=discord.Color.random()
        )
        embed.add_field(name="C1 乳酪粉紅醬(燉飯/義大利麵)", value="125", inline=True)
        embed.add_field(name="C2 唐揚野菇粉紅醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="C3 起司培根粉紅醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="C4 起司燻雞粉紅醬(燉飯/義大利麵)", value="145", inline=True)
        embed.add_field(name="C5 日式炸雞腿塊佐粉紅醬(燉飯/義大利麵)", value="155", inline=True)
        embed.add_field(name="C6 日式炸豬排佐粉紅醬(燉飯/義大利麵)", value="160", inline=True)
        embed.add_field(name="C7 蒜香蛤蜊佐粉紅醬(燉飯/義大利麵)", value="175", inline=True)
        embed.add_field(name="C8 海鮮總匯佐粉紅醬(燉飯/義大利麵)", value="180", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="紅醬系列", style=discord.ButtonStyle.secondary)
    async def button_red_sauce(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="紅醬系列",
            color=discord.Color.random()
        )
        embed.add_field(name="D1 經典茄汁義大利麵", value="125", inline=True)
        embed.add_field(name="D2 茄汁肉醬義大利麵", value="150", inline=True)
        embed.add_field(name="D3 海鮮總匯佐紅醬義大利麵", value="180", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="清炒系列", style=discord.ButtonStyle.secondary)
    async def button_stir_fry(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="清炒系列",
            color=discord.Color.random()
        )
        embed.add_field(name="E1 田園時蔬清炒義大利麵", value="145", inline=True)
        embed.add_field(name="E2 白酒蛤蜊清炒義大利麵", value="180", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="咖哩", style=discord.ButtonStyle.secondary)
    async def button_curry(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="咖哩",
            color=discord.Color.random()
        )
        embed.add_field(name="F1 鄉村雞肉咖哩飯", value="150", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="薄片披薩", style=discord.ButtonStyle.secondary)
    async def button_pizza(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="薄片披薩",
            color=discord.Color.random()
        )
        embed.add_field(name="G1 綜合菌菇松露披薩", value="155", inline=True)
        embed.add_field(name="G2 總匯披薩", value="155", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="單點", style=discord.ButtonStyle.secondary)
    async def button_addons(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="單點",
            color=discord.Color.random()
        )
        embed.add_field(name="當日例湯", value="60", inline=True)
        embed.add_field(name="美式辣雞翅", value="65", inline=True)
        embed.add_field(name="手工麵包盤(附果醬or奶油)", value="80", inline=True)
        embed.add_field(name="美式薯條", value="80", inline=True)
        embed.add_field(name="起司條", value="80", inline=True)
        embed.add_field(name="洋蔥圈", value="80", inline=True)
        embed.add_field(name="烤奶油玉米", value="100", inline=True)
        embed.add_field(name="香料綜合炒野菇", value="100", inline=True)
        embed.add_field(name="塔塔醬炸雞", value="120", inline=True)
        embed.add_field(name="松露薯條", value="120", inline=True)
        embed.add_field(name="塔塔醬魷魚圈", value="150", inline=True)
        embed.add_field(name="炸物共和國", value="220", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class SeaweedRiceRoll(discord.ui.View):
    def __init__(self):
        super().__init__()

    # Utility function to add footer to embeds
    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/10/5")
        return embed

    @discord.ui.button(label="海苔飯捲", style=discord.ButtonStyle.secondary)
    async def button_seaweed_rolls(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="海苔飯捲",
            color=discord.Color.random()
        )
        embed.add_field(name="肉鬆沙拉 飯捲", value="60", inline=True)
        embed.add_field(name="脆皮雞排 飯捲", value="75", inline=True)
        embed.add_field(name="起司蔬果(素) 飯捲", value="70", inline=True)
        embed.add_field(name="日式炸豬排 飯捲", value="75", inline=True)
        embed.add_field(name="起司鮪魚 飯捲", value="75", inline=True)
        embed.add_field(name="起司雞柳 飯捲", value="80", inline=True)
        embed.add_field(name="香香炸雞 飯捲", value="75", inline=True)
        embed.add_field(name="咔啦雞腿 飯捲", value="80", inline=True)
        embed.add_field(name="韓式烤肉 飯捲", value="75", inline=True)
        embed.add_field(name="泰式蝦排 飯捲", value="75", inline=True)
        embed.add_field(name="泡菜烤肉 飯捲", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="蔥抓餅", style=discord.ButtonStyle.secondary)
    async def button_cong_zhuabing(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="蔥抓餅",
            color=discord.Color.random()
        )
        embed.add_field(name="原味蔥抓餅", value="30", inline=True)
        embed.add_field(name="抓餅蛋", value="40", inline=True)
        embed.add_field(name="抓餅蛋 培根", value="50", inline=True)
        embed.add_field(name="抓餅蛋 鮪魚", value="60", inline=True)
        embed.add_field(name="抓餅蛋 九層塔", value="50", inline=True)
        embed.add_field(name="抓餅蛋 薯餅", value="60", inline=True)
        embed.add_field(name="抓餅蛋 玉米", value="50", inline=True)
        embed.add_field(name="抓餅蛋 泡菜", value="60", inline=True)
        embed.add_field(name="抓餅蛋 起司", value="50", inline=True)
        embed.add_field(name="抓餅蛋 烤肉", value="60", inline=True)
        embed.add_field(name="抓餅蛋 肉鬆", value="50", inline=True)
        embed.add_field(name="抓餅蛋 蝦排", value="60", inline=True)
        embed.add_field(name="抓餅蛋 高麗菜", value="50", inline=True)
        embed.add_field(name="抓餅蛋 咔啦", value="60", inline=True)
        embed.add_field(name="抓餅蛋 火腿", value="50", inline=True)
        embed.add_field(name="荷包蛋", value="15", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="中式甜不辣", style=discord.ButtonStyle.secondary)
    async def button_chinese_ten_potato(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="中式甜不辣",
            color=discord.Color.random()
        )
        embed.add_field(name="中式甜不辣", value="55 / 70", inline=True)
        embed.add_field(name="中式甜不辣 + 王子麵", value="70 / 85", inline=True)
        embed.add_field(name="中式甜不辣 + 冬粉", value="70 / 85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


    @discord.ui.button(label="酥炸類1", style=discord.ButtonStyle.secondary)
    async def button_deep_fried_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="酥炸類",
            color=discord.Color.random()
        )
        embed.add_field(name="地瓜球", value="40", inline=True)
        embed.add_field(name="蘿蔔糕", value="35", inline=True)
        embed.add_field(name="韭菜盒", value="40", inline=True)
        embed.add_field(name="雞排", value="80", inline=True)
        embed.add_field(name="甜不辣", value="30", inline=True)
        embed.add_field(name="青蔥龍捲餅", value="40", inline=True)
        embed.add_field(name="雞翅 (1支)", value="30", inline=True)
        embed.add_field(name="雞翅 (3支)", value="80", inline=True)
        embed.add_field(name="百頁豆腐", value="30", inline=True)
        embed.add_field(name="紅豆龍捲餅", value="40", inline=True)
        embed.add_field(name="香香炸雞", value="55", inline=True)
        embed.add_field(name="炸飯糰", value="40", inline=True)
        embed.add_field(name="檸檬雞柳條", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="酥炸類2", style=discord.ButtonStyle.secondary)
    async def button_deep_fried_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="酥炸類",
            color=discord.Color.random()
        )
        embed.add_field(name="雞米花", value="55", inline=True)
        embed.add_field(name="杏鮑菇", value="40", inline=True)
        embed.add_field(name="炸一口餃", value="35", inline=True)
        embed.add_field(name="薯條", value="40", inline=True)
        embed.add_field(name="炸湯圓", value="35", inline=True)
        embed.add_field(name="花枝丸", value="30", inline=True)
        embed.add_field(name="炸水餃", value="40", inline=True)
        embed.add_field(name="薯餅", value="40", inline=True)
        embed.add_field(name="熱狗", value="30", inline=True)
        embed.add_field(name="甘梅地瓜", value="40", inline=True)
        embed.add_field(name="麥克雞塊", value="35", inline=True)
        embed.add_field(name="豬血糕", value="30", inline=True)
        embed.add_field(name="銀絲卷煉乳", value="35", inline=True)
        embed.add_field(name="洋蔥圈", value="35", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)



    @discord.ui.button(label="每日一湯", style=discord.ButtonStyle.secondary)
    async def button_daily_soups(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="每日一湯",
            color=discord.Color.random()
        )
        embed.add_field(name="甜不辣湯", value="55", inline=True)
        embed.add_field(name="味噌湯", value="30", inline=True)
        embed.add_field(name="味噌貢丸湯", value="40", inline=True)
        embed.add_field(name="蘿蔔魚丸湯", value="40", inline=True)
        embed.add_field(name="魚丸冬粉湯", value="55", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


    @discord.ui.button(label="飲料類", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            color=discord.Color.random()
        )
        embed.add_field(name="冬瓜茶", value="20", inline=True)
        embed.add_field(name="紅茶(冰/熱)", value="20", inline=True)
        embed.add_field(name="奶綠(冰/熱)", value="25", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)



class Guguwaffle(discord.ui.View):
    def __init__(self):
        super().__init__()

    # Utility function to add footer to embeds
    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/5/30")
        return embed

    @discord.ui.button(label="抹醬系列", style=discord.ButtonStyle.secondary)
    async def button_spreads(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="抹醬系列",
            color=discord.Color.random()
        )
        embed.add_field(name="特製花生醬", value="瓦芙 50 / 鬆餅 80", inline=True)
        embed.add_field(name="頂級卡士達", value="瓦芙 50 / 鬆餅 80", inline=True)
        embed.add_field(name="香頌可可", value="瓦芙 50 / 鬆餅 80", inline=True)
        embed.add_field(name="日式抹茶", value="瓦芙 50 / 鬆餅 80", inline=True)
        embed.add_field(name="葡萄奶酥", value="瓦芙 45 / 鬆餅 75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="淋醬系列", style=discord.ButtonStyle.secondary)
    async def button_sauces(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="淋醬系列",
            color=discord.Color.random()
        )
        embed.add_field(name="果香蜂蜜", value="瓦芙 45 / 鬆餅 75", inline=True)
        embed.add_field(name="特調焦糖", value="瓦芙 50 / 鬆餅 80", inline=True)
        embed.add_field(name="風味煉乳", value="瓦芙 45 / 鬆餅 75", inline=True)
        embed.add_field(name="精選巧克力", value="瓦芙 45 / 鬆餅 75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="蔬菜系列", style=discord.ButtonStyle.secondary)
    async def button_vegetables(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="蔬菜系列",
            color=discord.Color.random()
        )
        embed.add_field(name="澳洲起司", value="瓦芙 45 / 鬆餅 75", inline=True)
        embed.add_field(name="起司蛋蛋蔬菜", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="田園起司玉米", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="和風鮪魚蔬菜", value="瓦芙 65 / 鬆餅 100", inline=True)
        embed.add_field(name="海苔肉鬆蔬菜", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="美國培根蔬菜", value="瓦芙 70 / 鬆餅 110", inline=True)
        embed.add_field(name="法式火腿蔬菜", value="瓦芙 65 / 鬆餅 100", inline=True)
        embed.add_field(name="德式香腸蔬菜", value="瓦芙 70 / 鬆餅 110", inline=True)
        embed.add_field(name="黑胡椒燻雞蔬菜", value="瓦芙 70 / 鬆餅 110", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="果醬系列", style=discord.ButtonStyle.secondary)
    async def button_jams(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="果醬系列",
            color=discord.Color.random()
        )
        embed.add_field(name="草莓果館", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="芒果果餡", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="焦糖蘋果", value="瓦芙 65 / 鬆餅 100", inline=True)
        embed.add_field(name="紅豆鮮奶油", value="瓦芙 50 / 鬆餅 80", inline=True)
        embed.add_field(name="藍莓果餡", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="特級檸檬果餡", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="蘋果果餡", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="肉桂蘋果", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="宇治金時", value="瓦芙 60 / 鬆餅 90", inline=True)
        embed.add_field(name="美味鮮奶球", value="瓦芙 45 / 鬆餅 75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飽足推薦", style=discord.ButtonStyle.secondary)
    async def button_recommendations(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飽足推薦",
            color=discord.Color.random()
        )
        embed.add_field(name="原味麻糬", value="鬆餅 130", inline=True)
        embed.add_field(name="黑糖麻糬餅", value="鬆餅 130", inline=True)
        embed.add_field(name="香酥原味", value="瓦芙 40 / 鬆餅 70", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="經典咖啡", style=discord.ButtonStyle.secondary)
    async def button_coffees(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="經典咖啡",
            color=discord.Color.random()
        )
        embed.add_field(name="美式咖啡", value="40", inline=True)
        embed.add_field(name="巧克力拿鐵", value="60", inline=True)
        embed.add_field(name="拿鐵", value="55", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="使用檸檬原汁", style=discord.ButtonStyle.secondary)
    async def button_lemon_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="檸檬原汁飲品",
            color=discord.Color.random()
        )
        embed.add_field(name="檸檬紅茶", value="45", inline=True)
        embed.add_field(name="檸檬綠茶", value="45", inline=True)
        embed.add_field(name="檸檬汁", value="45", inline=True)
        embed.add_field(name="蜂蜜檸檬", value="50", inline=True)
        embed.add_field(name="特調可可飲", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="現泡茶", style=discord.ButtonStyle.secondary)
    async def button_tea(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="現泡茶",
            color=discord.Color.random()
        )
        embed.add_field(name="錫蘭紅茶", value="30", inline=True)
        embed.add_field(name="茉黛綠茶", value="30", inline=True)
        embed.add_field(name="蜜茶", value="35", inline=True)
        embed.add_field(name="蜜香紅茶", value="45", inline=True)
        embed.add_field(name="蜜香綠茶", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="果醋系列", style=discord.ButtonStyle.secondary)
    async def button_vinegars(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="果醋系列",
            color=discord.Color.random()
        )
        embed.add_field(name="青梅果醋", value="40", inline=True)
        embed.add_field(name="丹荔果醋", value="40", inline=True)
        embed.add_field(name="蔓越梅果醋", value="40", inline=True)
        embed.add_field(name="玫瑰蘋果果醋", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="採用純鮮奶", style=discord.ButtonStyle.secondary)
    async def button_fresh_milk(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="鮮奶系列",
            color=discord.Color.random()
        )
        embed.add_field(name="鮮奶茶", value="55", inline=True)
        embed.add_field(name="鮮奶綠", value="55", inline=True)
        embed.add_field(name="蜜香鮮奶茶", value="60", inline=True)
        embed.add_field(name="蜜香鮮奶綠", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class SchoolBreakfast(discord.ui.View):
    def __init__(self):
        super().__init__()

    # Utility function to add footer to embeds
    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/5/22")
        return embed


    @discord.ui.button(label="超值套餐", style=discord.ButtonStyle.secondary)
    async def button_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="超值套餐",
            color=discord.Color.random()
        )
        embed.add_field(name="1號餐 咔啦雞腿堡+奶茶", value="85", inline=True)
        embed.add_field(name="2號餐 香雞蛋堡+奶茶", value="65", inline=True)
        embed.add_field(name="3號餐 火腿+蘿蔔糕+蛋+奶茶", value="60", inline=True)
        embed.add_field(name="4號餐 熱狗+蘿蔔糕+蛋+奶茶", value="60", inline=True)
        embed.add_field(name="5號餐 豬排+蘿蔔糕+蛋+奶茶", value="70", inline=True)
        embed.add_field(name="6號餐 鐵板麵 +蛋+香雞片+奶茶", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="蛋餅", style=discord.ButtonStyle.secondary)
    async def button_egg_pancakes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="蛋餅",
            description=" 加起士10元",
            color=discord.Color.random()
        )
        embed.add_field(name="原味蛋餅", value="30", inline=True)
        embed.add_field(name="培根蛋餅", value="40", inline=True)
        embed.add_field(name="火腿蛋餅", value="35", inline=True)
        embed.add_field(name="肉鬆蛋餅", value="35", inline=True)
        embed.add_field(name="薯餅蛋餅", value="45", inline=True)
        embed.add_field(name="豬排蛋餅", value="50", inline=True)
        embed.add_field(name="起士蛋餅", value="35", inline=True)
        embed.add_field(name="燻雞蛋餅", value="40", inline=True)
        embed.add_field(name="玉米蛋餅", value="35", inline=True)
        embed.add_field(name="鮪魚蛋餅", value="40", inline=True)
        embed.add_field(name="高麗菜蛋餅", value="35", inline=True)
        embed.add_field(name="大熱狗蛋餅", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)




    @discord.ui.button(label="漢堡", style=discord.ButtonStyle.secondary)
    async def button_burgers(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="漢堡",
            description="漢堡 加起士10元",
            color=discord.Color.random()
        )
        embed.add_field(name="漢堡蛋", value="45", inline=True)
        embed.add_field(name="香雞蛋堡", value="45", inline=True)
        embed.add_field(name="火腿蛋堡", value="40", inline=True)
        embed.add_field(name="薯餅蛋堡", value="50", inline=True)
        embed.add_field(name="培根蛋堡", value="40", inline=True)
        embed.add_field(name="里雞蛋堡", value="55", inline=True)
        embed.add_field(name="燻雞蛋堡", value="50", inline=True)
        embed.add_field(name="魚排蛋堡", value="50", inline=True)
        embed.add_field(name="豬排蛋堡", value="55", inline=True)
        embed.add_field(name="咔啦雞腿堡", value="65", inline=True)
        embed.add_field(name="牛肉吉士堡", value="60", inline=True)
        embed.add_field(name="綜合吉士堡", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="吐司", style=discord.ButtonStyle.secondary)
    async def button_toast(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="吐司",
            description="吐司 加起士10元",
            color=discord.Color.random()
        )
        embed.add_field(name="火腿蛋吐司", value="35", inline=True)
        embed.add_field(name="起士蛋吐司", value="35", inline=True)
        embed.add_field(name="培根蛋吐司", value="35", inline=True)
        embed.add_field(name="里雞排吐司", value="45", inline=True)
        embed.add_field(name="生菜蛋吐司", value="35", inline=True)
        embed.add_field(name="鮪魚蛋吐司", value="40", inline=True)
        embed.add_field(name="肉鬆蛋吐司", value="35", inline=True)
        embed.add_field(name="豬排蛋吐司", value="50", inline=True)
        embed.add_field(name="玉米蛋吐司", value="35", inline=True)
        embed.add_field(name="薯餅蛋吐司", value="45", inline=True)
        embed.add_field(name="烤總匯", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="鐵板麵", style=discord.ButtonStyle.secondary)
    async def button_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="鐵板麵",
            color=discord.Color.random()
        )
        embed.add_field(name="蘑菇麵+蛋+奶茶", value="70", inline=True)
        embed.add_field(name="黑胡椒麵+蛋+奶茶", value="70", inline=True)
        embed.add_field(name="義大利麵+蛋+奶茶", value="75", inline=True)
        embed.add_field(name="咖哩雞麵+蛋+奶茶", value="75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="可頌", style=discord.ButtonStyle.secondary)
    async def button_croissants(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="可頌",
            color=discord.Color.random()
        )
        embed.add_field(name="鮪魚可頌", value="45", inline=True)
        embed.add_field(name="豬排可頌", value="45", inline=True)
        embed.add_field(name="火腿起士可頌", value="45", inline=True)
        embed.add_field(name="培根起士可頌", value="45", inline=True)
        embed.add_field(name="起司帕瑪森", value="50", inline=True)
        embed.add_field(name="起司菠蘿堡", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="吐司/後片", style=discord.ButtonStyle.secondary)
    async def button_toast_spreads(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="吐司/後片",
            color=discord.Color.random()
        )
        embed.add_field(name="烤花生", value="20/25", inline=True)
        embed.add_field(name="烤巧克力", value="20/25", inline=True)
        embed.add_field(name="烤草莓", value="20/25", inline=True)
        embed.add_field(name="烤椰香", value="20/25", inline=True)
        embed.add_field(name="烤奶油", value="20/25", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="單品", style=discord.ButtonStyle.secondary)
    async def button_single_items(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="單品",
            color=discord.Color.random()
        )
        embed.add_field(name="蘿蔔糕", value="35", inline=True)
        embed.add_field(name="麥克雞塊(5個)", value="35", inline=True)
        embed.add_field(name="薯餅(5個)", value="40", inline=True)
        embed.add_field(name="熱狗蛋", value="35", inline=True)
        embed.add_field(name="咔啦雞腿塊", value="50", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飲料", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            color=discord.Color.random()
        )
        embed.add_field(name="紅茶", value="20", inline=True)
        embed.add_field(name="奶茶", value="25", inline=True)
        embed.add_field(name="豆漿", value="25", inline=True)
        embed.add_field(name="冬瓜茶", value="20", inline=True)
        embed.add_field(name="柳橙汁", value="25", inline=True)
        embed.add_field(name="阿華田", value="35", inline=True)
        embed.add_field(name="鮮奶紅茶", value="45", inline=True)
        embed.add_field(name="美式", value="35", inline=True)
        embed.add_field(name="拿鐵", value="50", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)





class Yuloong(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="套餐", style=discord.ButtonStyle.secondary)
    async def button_set_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="套餐",
            color=discord.Color.random()
        )
        embed.add_field(name="鍋貼套餐", value="102", inline=True)
        embed.add_field(name="水餃套餐", value="106", inline=True)
        embed.add_field(name="牛肉麵套餐", value="210", inline=True)
        embed.add_field(name="吞雲系列套餐", value="120", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="鍋貼", style=discord.ButtonStyle.secondary)
    async def button_potstickers(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="鍋貼",
            color=discord.Color.random()
        )
        embed.add_field(name="招牌(8顆)", value="52", inline=True)
        embed.add_field(name="韓式辣味(8顆)", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="麵類", style=discord.ButtonStyle.secondary)
    async def button_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="川味椒麻拌麵", value="50", inline=True)
        embed.add_field(name="酢醬麵", value="65", inline=True)
        embed.add_field(name="酸辣麵", value="75", inline=True)
        embed.add_field(name="清燉牛肉麵", value="160", inline=True)
        embed.add_field(name="紅燒牛肉麵", value="160", inline=True)
        embed.add_field(name="麻辣牛肉麵", value="170", inline=True)
        embed.add_field(name="清燉牛三寶麵", value="190", inline=True)
        embed.add_field(name="紅燒牛三寶麵", value="190", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="水餃", style=discord.ButtonStyle.secondary)
    async def button_dumplings(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="水餃",
            color=discord.Color.random()
        )
        embed.add_field(name="高麗菜(8顆)", value="56", inline=True)
        embed.add_field(name="韭菜(8顆)", value="56", inline=True)
        embed.add_field(name="蔬菜(8顆)", value="56", inline=True)
        embed.add_field(name="玉米(8顆)", value="56", inline=True)
        embed.add_field(name="韓式辣味(8顆)", value="60", inline=True)
        embed.add_field(name="剝皮辣椒雞(8顆)", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)



    @discord.ui.button(label="蒸餃", style=discord.ButtonStyle.secondary)
    async def button_steamed_dumplings(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="蒸餃",
            color=discord.Color.random()
        )
        embed.add_field(name="酸辣湯餃(6顆)", value="90", inline=True)
        embed.add_field(name="玉米湯餃(6顆)", value="90", inline=True)
        embed.add_field(name="牛肉湯餃(7顆)", value="90", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯品", style=discord.ButtonStyle.secondary)
    async def button_soups(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯品",
            color=discord.Color.random()
        )
        embed.add_field(name="酸辣湯", value="35", inline=True)
        embed.add_field(name="玉米濃湯", value="35", inline=True)
        embed.add_field(name="剝皮辣椒雞湯", value="75", inline=True)
        embed.add_field(name="牛肉湯(3塊牛肉)", value="80", inline=True)
        embed.add_field(name="麻油雞腿湯", value="85", inline=True)
        embed.add_field(name="香菇雞腿湯", value="85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="小菜", style=discord.ButtonStyle.secondary)
    async def button_sides(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="小菜",
            color=discord.Color.random()
        )
        embed.add_field(name="滷蛋", value="15", inline=True)
        embed.add_field(name="燙青菜", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)




class JapaneseFood(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/10/21")
        return embed

    @discord.ui.button(label="主廚推薦", style=discord.ButtonStyle.secondary)
    async def button_specialty_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="主廚推薦",
            color=discord.Color.random()
        )
        embed.add_field(name="黃悶雞腿飯", value="135", inline=True)
        embed.add_field(name="香酥雞腿飯", value="140", inline=True)
        embed.add_field(name="紐澳良雞腿排飯", value="130", inline=True)
        embed.add_field(name="三杯雞飯", value="130", inline=True)
        embed.add_field(name="咖哩烏龍麵", value="130", inline=True)
        embed.add_field(name="麻辣牛肉麵", value="135", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="特色餐", style=discord.ButtonStyle.secondary)
    async def button_specialty_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="特色餐",
            color=discord.Color.random()
        )
        embed.add_field(name="炸醬麵", value="80", inline=True)
        embed.add_field(name="打拋豬飯", value="110", inline=True)
        embed.add_field(name="厚片豬排飯", value="110", inline=True)
        # embed.add_field(name="雪魚排飯", value="110", inline=True)
        embed.add_field(name="椒麻雞腿飯", value="130", inline=True)
        embed.add_field(name="上海紅燒肉飯", value="135", inline=True)
        embed.add_field(name="照燒烤牛肉飯", value="135", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="拉麵類", style=discord.ButtonStyle.secondary)
    async def button_ramen(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="拉麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="村吉蔬菜拉麵/烏龍麵", value="90", inline=True)
        embed.add_field(name="玉米海苔拉麵/烏龍麵", value="110", inline=True)
        embed.add_field(name="厚片豬排拉麵/烏龍麵", value="125", inline=True)
        embed.add_field(name="牛五花肉拉麵/烏龍麵", value="135", inline=True)
        embed.add_field(name="叉燒肉拉麵/烏龍麵", value="135", inline=True)
        embed.add_field(name="照燒烤牛肉拉麵/烏龍麵", value="135", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="咖哩飯類", style=discord.ButtonStyle.secondary)
    async def button_curry_rice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="咖哩飯類",
            color=discord.Color.random()
        )
        embed.add_field(name="村吉咖哩飯", value="85", inline=True)
        embed.add_field(name="歐姆蛋咖哩飯", value="120", inline=True)
        embed.add_field(name="厚片豬排咖哩飯", value="125", inline=True)
        # embed.add_field(name="漢堡排咖哩飯", value="125", inline=True)
        embed.add_field(name="唐揚炸雞咖哩飯", value="125", inline=True)
        # embed.add_field(name="牛腱肉咖哩飯", value="135", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="丼飯類", style=discord.ButtonStyle.secondary)
    async def button_donburi(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="丼飯類",
            color=discord.Color.random()
        )
        embed.add_field(name="厚片豬排丼飯", value="120", inline=True)
        embed.add_field(name="唐揚炸雞丼飯", value="120", inline=True)
        embed.add_field(name="牛五花肉丼飯", value="135", inline=True)
        embed.add_field(name="照燒牛五花肉丼飯", value="135", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

#    @discord.ui.button(label="點心類", style=discord.ButtonStyle.secondary)
#    async def button_snacks(self, interaction: discord.Interaction, button: discord.ui.Button):
#        embed = discord.Embed(
#            title="點心類",
#            color=discord.Color.random()
#        )
#        embed.add_field(name="南瓜可樂餅", value="45", inline=True)
#        # embed.add_field(name="蔬菜可樂餅", value="45", inline=True)
#        # embed.add_field(name="洋蔥圈", value="50", inline=True)
#        # embed.add_field(name="起司可樂餅", value="60", inline=True)
#        embed = self.add_footer(embed)
#        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="點心/飲料/湯類", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="點心/飲料/湯類",
            color=discord.Color.random()
        )
        embed.add_field(name="南瓜可樂餅", value="45", inline=True)
        embed.add_field(name="泰國奶茶", value="55", inline=True)
        embed.add_field(name="冬瓜茶", value="30", inline=True)
        embed.add_field(name="冬瓜烏龍茶", value="30", inline=True)
        embed.add_field(name="烏龍茶", value="35", inline=True)
        embed.add_field(name="味增湯", value="10", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class Grateful(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="餃類", style=discord.ButtonStyle.secondary)
    async def button_gyoza(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="餃類",
            color=discord.Color.random()
        )
        
        embed.add_field(name="水餃", value="每粒 5", inline=True)
        embed.add_field(name="鮮蝦餛飩", value="每粒 5", inline=True)
        embed.add_field(name="紅油抄手", value="60", inline=True)
        embed.add_field(name="抄手(不辣)", value="60", inline=True)
        embed.add_field(name="紅油抄手麵(辣)", value="70", inline=True)
        embed.add_field(name="抄手麵(不辣)", value="70", inline=True)
        embed.add_field(name="牛肉湯餃", value="大 120/ 中 100/ 小 75", inline=True)
        embed.add_field(name="酸辣湯餃", value="大 120/ 中 100/ 小 75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="麵類", style=discord.ButtonStyle.secondary)
    async def button_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="牛肉麵", value="大 120/ 小 100", inline=True)
        embed.add_field(name="牛肉冬粉", value="大 120/ 小 100", inline=True)
        embed.add_field(name="酸辣冬粉", value="大 80/ 小 65", inline=True)
        embed.add_field(name="酸辣拉麵", value="大 80/ 小 65", inline=True)
        embed.add_field(name="炸醬冬粉", value="大 80/ 小 65", inline=True)
        embed.add_field(name="炸醬拉麵", value="大 80/ 小 65", inline=True)
        embed.add_field(name="牛肉湯拉麵", value="大 80/ 小 65", inline=True)
        embed.add_field(name="牛肉湯冬粉", value="大 80/ 小 65", inline=True)
        embed.add_field(name="鮮蝦餛飩麵", value="大 80/ 小 65", inline=True)
        embed.add_field(name="鮮蝦餛飩冬粉", value="大 80/ 小 65", inline=True)
        embed.add_field(name="赤肉冬粉湯", value="大 80/ 小 65", inline=True)
        embed.add_field(name="赤肉麵", value="大 80/ 小 65", inline=True)
        embed.add_field(name="肉燥乾麵", value="大 60/ 小 45", inline=True)
        embed.add_field(name="肉燥乾冬粉", value="大 60/ 小 45", inline=True)
        embed.add_field(name="紅油乾麵(無肉)", value="大 60/ 小 45", inline=True)
        embed.add_field(name="紅油乾冬粉(無肉)", value="大 60/ 小 45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯類", style=discord.ButtonStyle.secondary)
    async def button_soups(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯類",
            color=discord.Color.random()
        )
        embed.add_field(name="酸辣湯", value="40", inline=True)
        embed.add_field(name="牛肉清湯(沒肉)", value="50", inline=True)
        embed.add_field(name="牛肉湯(有肉)", value="70", inline=True)
        embed.add_field(name="赤肉薑絲湯", value="50", inline=True)
        embed.add_field(name="牛肉湯餛飩", value="60", inline=True)
        embed.add_field(name="鮮蝦餛飩湯", value="50", inline=True)
        embed.add_field(name="榨菜肉絲湯", value="40", inline=True)
        embed.add_field(name="牛肉餛飩湯", value="100", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飯類", style=discord.ButtonStyle.secondary)
    async def button_rice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飯類",
            description="蓋飯可三選一   豬耳/青菜/綜合",
            color=discord.Color.random()
        )
        embed.add_field(name="魯肉飯", value="大 45/ 小 35", inline=False)
        embed.add_field(name="牛肉蓋飯", value="100", inline=True)
        embed.add_field(name="蒜泥白肉蓋飯", value="80", inline=True)
        embed.add_field(name="烤肉蓋飯", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="小菜類", style=discord.ButtonStyle.secondary)
    async def button_side_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="小菜類",
            color=discord.Color.random()
        )
        embed.add_field(name="滷牛肉", value="60", inline=True)
        embed.add_field(name="蒜泥白肉", value="50", inline=True)
        embed.add_field(name="皮蛋豆腐", value="40", inline=True)
        embed.add_field(name="豬耳朵", value="40", inline=True)
        embed.add_field(name="豆干", value="15", inline=True)
        embed.add_field(name="油豆腐", value="15", inline=True)
        embed.add_field(name="海帶", value="15", inline=True)
        embed.add_field(name="滷蛋", value="15", inline=True)
        embed.add_field(name="燙空心菜", value="30", inline=True)
        embed.add_field(name="燙小白菜", value="30", inline=True)
        embed.add_field(name="燙豆芽菜", value="30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

class HappyBreakfast(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed
    @discord.ui.button(label="套餐", style=discord.ButtonStyle.secondary)
    async def button_combo_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="套餐",
            description="""套餐附20元飲料  
            冰/熱奶茶  冰/熱紅茶  百香果汁""",
            color=discord.Color.random()
        )
        embed.add_field(name="火腿三明治", value="55", inline=True)
        embed.add_field(name="豬排三明治", value="55", inline=True)
        embed.add_field(name="鮪魚三明治", value="55", inline=True)
        embed.add_field(name="香雞三明治", value="55", inline=True)
        embed.add_field(name="培根三明治", value="55", inline=True)
        embed.add_field(name="起司蛋餅", value="55", inline=True)
        embed.add_field(name="椒鹽菲力雞堡", value="60", inline=True)
        embed.add_field(name="豬肉漢堡", value="55", inline=True)
        embed.add_field(name="紐奧良雞腿堡", value="70", inline=True)
        embed.add_field(name="泰式檸檬雞腿堡", value="70", inline=True)
        embed.add_field(name="薯餅三明治", value="55", inline=True)
        embed.add_field(name="大鱈魚起司堡", value="70", inline=True)
        embed.add_field(name="燻雞三明治", value="60", inline=True)
        embed.add_field(name="藍帶豬排堡", value="75", inline=True)
        embed.add_field(name="水牛城雞腿堡", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="漢堡", style=discord.ButtonStyle.secondary)
    async def button_burgers(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="漢堡",
            description="漢堡加蛋+15",
            color=discord.Color.random()
        )
        embed.add_field(name="豬肉漢堡", value="30", inline=True)
        embed.add_field(name="香雞漢堡", value="35", inline=True)
        embed.add_field(name="豬排漢堡", value="35", inline=True)
        embed.add_field(name="椒鹽菲力雞漢堡", value="35", inline=True)
        embed.add_field(name="鮪魚漢堡", value="35", inline=True)
        embed.add_field(name="柚香花枝堡", value="40", inline=True)
        embed.add_field(name="紐奧良雞腿堡", value="45", inline=True)
        embed.add_field(name="泰式檸檬雞腿堡", value="45", inline=True)
        embed.add_field(name="明太子蝦排堡", value="45", inline=True)
        embed.add_field(name="藍帶豬排堡", value="50", inline=True)
        embed.add_field(name="卡啦雞腿堡", value="50", inline=True)
        embed.add_field(name="大鱈魚起司堡", value="55", inline=True)
        embed.add_field(name="水牛城雞腿堡", value="55", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="三明治", style=discord.ButtonStyle.secondary)
    async def button_sandwiches(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="三明治",
            description="三明治加蛋+15",
            color=discord.Color.random()
        )
        embed.add_field(name="蔬菜蛋三明治", value="30", inline=True)
        embed.add_field(name="總匯三明治(有蛋)", value="65", inline=True)
        embed.add_field(name="肉鬆三明治", value="25", inline=True)
        embed.add_field(name="火腿三明治", value="30", inline=True)
        embed.add_field(name="培根三明治", value="30", inline=True)
        embed.add_field(name="薯餅三明治", value="30", inline=True)
        embed.add_field(name="香雞三明治", value="30", inline=True)
        embed.add_field(name="鮪魚三明治", value="35", inline=True)
        embed.add_field(name="燻雞三明治", value="35", inline=True)
        embed.add_field(name="豬排三明治", value="35", inline=True)
        embed.add_field(name="花枝三明治", value="35", inline=True)
        embed.add_field(name="菲力雞三明治", value="35", inline=True)
        embed.add_field(name="明太子蝦排三明治", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="中式餐點", style=discord.ButtonStyle.secondary)
    async def button_chinese_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="中式餐點",
            color=discord.Color.random()
        )
        embed.add_field(name="原味蛋餅", value="30", inline=True)
        embed.add_field(name="薯餅蛋餅", value="45", inline=True)
        embed.add_field(name="起司蛋餅", value="40", inline=True)
        embed.add_field(name="鮪魚蛋餅", value="50", inline=True)
        embed.add_field(name="玉米蛋餅", value="40", inline=True)
        embed.add_field(name="肉鬆蛋餅", value="40", inline=True)
        embed.add_field(name="燻雞蛋餅", value="50", inline=True)
        embed.add_field(name="火腿蛋餅", value="45", inline=True)
        embed.add_field(name="豬排蛋餅", value="50", inline=True)
        embed.add_field(name="培根蛋餅", value="45", inline=True)
        embed.add_field(name="日式煎餃", value="30", inline=True)
        embed.add_field(name="港式蘿蔔糕", value="30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)



    @discord.ui.button(label="現炒鐵板麵", style=discord.ButtonStyle.secondary)
    async def button_iron_plate_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="現炒鐵板麵",
            color=discord.Color.random()
        )
        embed.add_field(name="黑胡椒醬鐵板麵(加蛋)", value="65", inline=True)
        embed.add_field(name="磨菇醬鐵板麵(加蛋)", value="65", inline=True)
        embed.add_field(name="培根鐵板麵(黑胡椒/磨菇醬)", value="65/加蛋 80", inline=True)
        embed.add_field(name="豬排鐵板麵(黑胡椒/磨菇醬)", value="65/加蛋 80", inline=True)
        embed.add_field(name="香雞鐵板麵(黑胡椒/磨菇醬)", value="65/加蛋 80", inline=True)
        embed.add_field(name="花枝鐵板麵(黑胡椒/磨菇醬)", value="65/加蛋 80", inline=True)
        embed.add_field(name="XO牛肉醬鐵板麵(加蛋)", value="75", inline=True)
        embed.add_field(name="奶油培根醬鐵板麵(加蛋)", value="75", inline=True)
        embed.add_field(name="宮保雞丁醬鐵板麵(加蛋)", value="75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="果醬吐司/現烤厚片", style=discord.ButtonStyle.secondary)
    async def button_toasts(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="果醬吐司/現烤厚片",
            color=discord.Color.random()
        )
        embed.add_field(name="草莓", value="17/30", inline=True)
        embed.add_field(name="花生", value="17/30", inline=True)
        embed.add_field(name="巧克力", value="17/30", inline=True)
        embed.add_field(name="奶酥", value="17/30", inline=True)
        embed.add_field(name="奶油", value="17/30", inline=True)
        embed.add_field(name="香蒜", value="17/30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


    @discord.ui.button(label="小吃", style=discord.ButtonStyle.secondary)
    async def button_snacks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="小吃",
            color=discord.Color.random()
        )
        embed.add_field(name="港式西多士(花生/巧克力)", value="45", inline=True)
        embed.add_field(name="美國薯餅", value="20", inline=True)
        embed.add_field(name="小熱狗(四條)", value="25", inline=True)
        embed.add_field(name="小雞塊(五塊)", value="35", inline=True)
        embed.add_field(name="煎荷包蛋", value="20", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)





    @discord.ui.button(label="飲料", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            description="皆為中杯 大杯+5",
            color=discord.Color.random()
        )
        embed.add_field(name="冰/熱奶茶", value="20", inline=True)
        embed.add_field(name="冰/熱紅茶", value="20", inline=True)
        embed.add_field(name="百香果汁", value="20", inline=True)
        embed.add_field(name="柳橙汁", value="25", inline=True)
        embed.add_field(name="韓式柚子紅茶", value="25", inline=True)
        embed.add_field(name="港式檸檬紅茶", value="25", inline=True)
        embed.add_field(name="港式鴛鴦奶茶", value="30", inline=True)
        embed.add_field(name="阿華田", value="30", inline=True)
        embed.add_field(name="鮮奶茶", value="30", inline=True)
        embed.add_field(name="港式檸檬七喜", value="30", inline=True)
        embed.add_field(name="港式檸檬可樂", value="30", inline=True)
        embed.add_field(name="冰/熱咖啡牛奶", value="30", inline=True)
        embed.add_field(name="豆漿(僅有中杯)", value="20", inline=True)
        embed.add_field(name="可樂", value="20", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    


class MOMOBreakfast(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/9/25")
        return embed

    @discord.ui.button(label="人氣特餐", style=discord.ButtonStyle.secondary)
    async def button_popular_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="人氣特餐",
            description="""加起司+10元 加花生+10元
以上客餐均附20元飲料(飲料區挑選) 不須飲料~15元為單點價格
""",
            color=discord.Color.random()
        )
        embed.add_field(name="A餐 薯餅蛋三明治", value="60", inline=True)
        embed.add_field(name="B餐 鱈魚起司蛋堡", value="75", inline=True)
        embed.add_field(name="C餐 醬燒雞腿蛋堡", value="75", inline=True)
        embed.add_field(name="D餐 德國香腸蛋堡", value="75", inline=True)
        embed.add_field(name="E餐 菲力雞排蛋三明治", value="70", inline=True)
        embed.add_field(name="F餐 卡啦雞腿蛋堡", value="75", inline=True)
        embed.add_field(name="G餐 泰式花枝蛋堡", value="65", inline=True)
        embed.add_field(name="H餐 鮮蝦蛋堡", value="65", inline=True)
        embed.add_field(name="I餐 起司豬排蛋堡", value="75", inline=True)
        embed.add_field(name="J餐 紐澳良雞腿蛋堡", value="75", inline=True)
        embed.add_field(name="K餐 四盎司牛肉蛋堡", value="90", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="超值特餐", style=discord.ButtonStyle.secondary)
    async def button_value_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="超值特餐",
            description="""加起司+10元 加花生+10元
以上客餐均附20元飲料(飲料區挑選) 不須飲料~15元為單點價格
""",
            color=discord.Color.random()
        )
        embed.add_field(name="1號餐 火腿蛋三明治", value="55", inline=True)
        embed.add_field(name="2號餐 豬排蛋三明治", value="60", inline=True)
        embed.add_field(name="3號餐 鮪魚蛋三明治", value="60", inline=True)
        embed.add_field(name="4號餐 香雞蛋三明治", value="60", inline=True)
        embed.add_field(name="5號餐 培根蛋三明治", value="55", inline=True)
        embed.add_field(name="6號餐 起司蛋餅", value="50", inline=True)
        embed.add_field(name="7號餐 義式香草雞腿蛋堡", value="75", inline=True)
        embed.add_field(name="6號餐 豬肉蛋漢堡", value="55", inline=True)
        embed.add_field(name="9號餐 燻雞蛋三明治", value="60", inline=True)
        embed.add_field(name="10號餐 泰式檸檬雞腿蛋堡", value="75", inline=True)
        embed.add_field(name="11號餐 日式雞排蛋堡", value="75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="蛋餅", style=discord.ButtonStyle.secondary)
    async def button_egg_pancakes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="蛋餅",
            color=discord.Color.random()
        )
        embed.add_field(name="原味蛋餅", value="25", inline=True)
        embed.add_field(name="起司蛋餅", value="35", inline=True)
        embed.add_field(name="玉米蛋餅", value="35", inline=True)
        embed.add_field(name="火腿蛋餅", value="40", inline=True)
        embed.add_field(name="培根蛋餅", value="40", inline=True)
        embed.add_field(name="肉鬆蛋餅", value="40", inline=True)
        embed.add_field(name="薯餅蛋餅", value="45", inline=True)
        embed.add_field(name="鮪魚蛋餅", value="45", inline=True)
        embed.add_field(name="豬排蛋餅", value="45", inline=True)
        embed.add_field(name="燻雞蛋餅", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="三明治", style=discord.ButtonStyle.secondary)
    async def button_sandwiches(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="三明治",
            description="三明治	加蛋+10",
            color=discord.Color.random()
        )
        embed.add_field(name="蔬菜蛋三明治", value="35", inline=True)
        embed.add_field(name="肉鬆三明治", value="30", inline=True)
        embed.add_field(name="火腿三明治", value="30", inline=True)
        embed.add_field(name="培根三明治", value="30", inline=True)
        embed.add_field(name="鮪魚三明治", value="35", inline=True)
        embed.add_field(name="香雞三明治", value="35", inline=True)
        embed.add_field(name="燻雞三明治", value="35", inline=True)
        embed.add_field(name="豬排三明治", value="35", inline=True)
        embed.add_field(name="花枝三明治", value="40", inline=True)
        embed.add_field(name="鮮蝦三明治", value="40", inline=True)
        embed.add_field(name="總匯三明治", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label="漢堡", style=discord.ButtonStyle.secondary)
    async def button_burgers(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="漢堡",
            description="漢堡  加蛋+10",
            color=discord.Color.random()
        )
        embed.add_field(name="豬肉漢堡", value="30", inline=True)
        embed.add_field(name="火腿漢堡", value="30", inline=True)
        embed.add_field(name="培根漢堡", value="30", inline=True)
        embed.add_field(name="鮪魚漢堡", value="35", inline=True)
        embed.add_field(name="香雞漢堡", value="35", inline=True)
        embed.add_field(name="燻雞漢堡", value="35", inline=True)
        embed.add_field(name="豬排漢堡", value="35", inline=True)
        embed.add_field(name="椒鹽菲力雞漢堡", value="35", inline=True)
        embed.add_field(name="鮪魚漢堡", value="35", inline=True)
        embed.add_field(name="明太子蝦排漢堡", value="40", inline=True)
        embed.add_field(name="藍帶豬排漢堡", value="50", inline=True)
        embed.add_field(name="卡啦雞腿漢堡", value="50", inline=True)
        embed.add_field(name="大鱈魚起司漢堡", value="55", inline=True)
        embed.add_field(name="水牛城雞腿漢堡", value="55", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="現炒鐵板麵", style=discord.ButtonStyle.secondary)
    async def button_iron_plate_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="現炒鐵板麵",
            description="""加蛋+10 以上套餐均附20元飲料
""",
            color=discord.Color.random()
        )
        embed.add_field(name="蘑菇鐵板麵(有蛋)", value="75", inline=True)
        embed.add_field(name="培根蘑菇鐵板麵", value="85", inline=True)
        embed.add_field(name="豬排蘑菇鐵板麵", value="85", inline=True)
        embed.add_field(name="香雞蘑菇鐵板麵", value="85", inline=True)
        embed.add_field(name="花枝蘑菇鐵板麵", value="85", inline=True)
        embed.add_field(name="XO牛肉醬鐵板麵", value="85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="果醬/厚片吐司", style=discord.ButtonStyle.secondary)
    async def button_toasts(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="果醬吐司/現烤厚片",
            color=discord.Color.random()
        )
        embed.add_field(name="草莓", value="20/30", inline=True)
        embed.add_field(name="花生", value="20/30", inline=True)
        embed.add_field(name="巧克力", value="20/30", inline=True)
        embed.add_field(name="奶酥", value="20/30", inline=True)
        embed.add_field(name="奶油", value="20/30", inline=True)
        embed.add_field(name="香蒜", value="20/30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    
    @discord.ui.button(label="炸物點心", style=discord.ButtonStyle.secondary)
    async def button_snacks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="炸物點心",
            color=discord.Color.random()
        )
        embed.add_field(name="全/半熟蛋", value="15", inline=True)
        embed.add_field(name="散蛋", value="15", inline=True)
        embed.add_field(name="熱狗", value="20", inline=True)
        embed.add_field(name="煎餃", value="35", inline=True)
        embed.add_field(name="港式蘿蔔糕", value="35", inline=True)
        embed.add_field(name="雞塊", value="40", inline=True)
        embed.add_field(name="薯條", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飲料", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            description="皆為中杯 大杯+5",
            color=discord.Color.random()
        )
        embed.add_field(name="冰/熱紅茶", value="20", inline=True)
        embed.add_field(name="冰/熱奶茶", value="20", inline=True)
        embed.add_field(name="豆漿", value="20", inline=True)
        embed.add_field(name="港式駕鴦奶茶", value="25", inline=True)
        embed.add_field(name="檸檬紅茶", value="25", inline=True)
        embed.add_field(name="咖啡牛奶", value="35", inline=True)
        embed.add_field(name="鮮奶茶", value="35", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class Pi_k(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="主餐系列", style=discord.ButtonStyle.secondary)
    async def button_main_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="主餐系列",
            description="""☆一份餐點只限一種口味☆
胡椒  香蒜  咖哩  起士  梅粉  海苔
並選擇是否加辣""",
            color=discord.Color.random()
        )
        embed.add_field(name="脆皮雞排", value="85", inline=True)
        embed.add_field(name="脆皮雞排塊", value="75", inline=True)
        embed.add_field(name="脆皮鮮魷", value="75", inline=True)
        embed.add_field(name="脆皮小雞翅(兩支)", value="70", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="點心系列", style=discord.ButtonStyle.secondary)
    async def button_snacks_series(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="點心系列",
            description="""☆一份餐點只限一種口味☆
胡椒  梅粉  並選擇是否加辣""",
            color=discord.Color.random()
        )
        embed.add_field(name="米血糕", value="25", inline=True)
        embed.add_field(name="芋香地瓜球", value="25", inline=True)
        embed.add_field(name="梅子地瓜條", value="25", inline=True)
        embed.add_field(name="脆皮甜不辣", value="25", inline=True)
        embed.add_field(name="脆皮百頁豆腐", value="25", inline=True)
        embed.add_field(name="脆皮花枝丸", value="25", inline=True)
        embed.add_field(name="脆皮米腸", value="25", inline=True)
        embed.add_field(name="花生粉小湯圓", value="25", inline=True)
        embed.add_field(name="雞皮", value="30", inline=True)
        embed.add_field(name="雞屁股", value="30", inline=True)
        embed.add_field(name="雞心", value="30", inline=True)
        embed.add_field(name="四季豆", value="30", inline=True)
        embed.add_field(name="炸玉米", value="30", inline=True)
        embed.add_field(name="炸青椒", value="30", inline=True)
        embed.add_field(name="脆皮杏鮑菇", value="30", inline=True)
        embed.add_field(name="脆皮馬鈴薯條", value="35", inline=True)
        embed.add_field(name="起司條(3條)", value="35", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class Longlong(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed


    @discord.ui.button(label="飯類", style=discord.ButtonStyle.secondary)
    async def button_rice_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飯類",
            color=discord.Color.random()
        )
        embed.add_field(name="魯肉飯", value="25", inline=True)
        embed.add_field(name="宮保雞丁蓋飯", value="75", inline=True)
        embed.add_field(name="滷排骨蓋飯", value="75", inline=True)
        embed.add_field(name="香辣翅腿蓋飯", value="75", inline=True)
        embed.add_field(name="養生餐", value="80", inline=True)
        embed.add_field(name="香油雞腿飯", value="90", inline=True)
        embed.add_field(name="香酥雞腿飯", value="90", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="麵類", style=discord.ButtonStyle.secondary)
    async def button_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="宮保雞丁乾麵", value="75", inline=True)
        embed.add_field(name="滷排骨乾麵", value="75", inline=True)
        embed.add_field(name="香辣翅腿乾麵", value="75", inline=True)
        embed.add_field(name="和風涼麵", value="50", inline=True)
        embed.add_field(name="乾麵", value="30", inline=True)
        embed.add_field(name="鍋邊素面", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="海鮮", style=discord.ButtonStyle.secondary)
    async def button_seafood(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="海鮮",
            color=discord.Color.random()
        )
        embed.add_field(name="麵", value="85", inline=True)
        embed.add_field(name="细粉", value="85", inline=True)
        embed.add_field(name="泡飯", value="85", inline=True)
        embed.add_field(name="米粉", value="85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="酸辣湯", style=discord.ButtonStyle.secondary)
    async def button_hot_sour_soup(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="酸辣湯",
            color=discord.Color.random()
        )
        embed.add_field(name="麺", value="50", inline=True)
        embed.add_field(name="米粉", value="50", inline=True)
        embed.add_field(name="泡飯", value="50", inline=True)
        embed.add_field(name="餃", value="65/85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="小菜/水餃", style=discord.ButtonStyle.secondary)
    async def button_side_dishes_dumplings(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="小菜/水餃",
            color=discord.Color.random()
        )
        embed.add_field(name="手工水餃(個)", value="5", inline=True)
        embed.add_field(name="皮蛋豆腐", value="35", inline=True)
        embed.add_field(name="燙青菜", value="30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯", style=discord.ButtonStyle.secondary)
    async def button_soups(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯類",
            color=discord.Color.random()
        )
        embed.add_field(name="豬肝湯", value="40", inline=True)
        embed.add_field(name="蛤蠣湯", value="40", inline=True)
        embed.add_field(name="酸辣湯", value="30", inline=True)
        embed.add_field(name="青菜蛋花湯", value="30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飲料", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            color=discord.Color.random()
        )
        embed.add_field(name="招牌紅茶冰", value="25", inline=True)
        embed.add_field(name="回味冬瓜茶", value="25", inline=True)
        embed.add_field(name="無糖綠茶", value="25", inline=True)
        embed.add_field(name="檸檬原汁水", value="25", inline=True)
        embed.add_field(name="鮮奶紅茶冰", value="35", inline=True)
        embed.add_field(name="豆漿紅茶冰", value="35", inline=True)
        embed.add_field(name="檸檬紅茶冰", value="35", inline=True)
        embed.add_field(name="蘋果牛奶紅茶冰", value="35", inline=True)
        embed.add_field(name="巧克力紅茶冰", value="35", inline=True)
        embed.add_field(name="鮮奶冬瓜茶", value="35", inline=True)
        embed.add_field(name="豆漿冬瓜茶", value="35", inline=True)
        embed.add_field(name="檸檬冬瓜茶", value="35", inline=True)
        embed.add_field(name="蘋果牛奶冬瓜茶", value="35", inline=True)
        embed.add_field(name="巧克力冬瓜茶", value="35", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)
    
    @discord.ui.button(label="冬季限定飲品", style=discord.ButtonStyle.secondary)
    async def button_winter_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="冬季限定飲品",
            color=discord.Color.random()
        )
        embed.add_field(name="熱!红茶", value="20", inline=True)
        embed.add_field(name="熱!鮮奶紅茶", value="30", inline=True)
        embed.add_field(name="香辣翅腿", value="30", inline=True)
        embed.add_field(name="豬耳朵", value="30", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)



class Kitchen_3(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="羹+主食", style=discord.ButtonStyle.secondary)
    async def button_geng_main(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="羹+主食",
            description="主食可選 飯/麺/米粉/冬粉/板條",
            color=discord.Color.random()
        )
        embed.add_field(name="羊肉羹", value="90/110", inline=True)
        embed.add_field(name="鱿魚羹", value="70/90", inline=True)
        embed.add_field(name="綜合羹", value="105/125", inline=True)
        embed.add_field(name="雞絲羹", value="70/90", inline=True)
        embed.add_field(name="肉羹", value="70/90", inline=True)
        embed.add_field(name="清羹", value="50", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="羹湯", style=discord.ButtonStyle.secondary)
    async def button_geng_soup(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="羹湯",
            color=discord.Color.random()
        )
        embed.add_field(name="羊肉羹", value="80", inline=True)
        embed.add_field(name="鱿魚羹", value="60", inline=True)
        embed.add_field(name="綜合羹", value="95", inline=True)
        embed.add_field(name="雞絲羹", value="60", inline=True)
        embed.add_field(name="肉羹", value="60", inline=True)
        embed.add_field(name="清羹", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯麵類", style=discord.ButtonStyle.secondary)
    async def button_noodle_soup(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯麵類",
            description="可選米粉、冬粉",
            color=discord.Color.random()
        )
        embed.add_field(name="擔仔麺", value="65/80", inline=True)
        embed.add_field(name="薑絲肉片湯麺", value="65/80", inline=True)
        embed.add_field(name="貢丸湯麺", value="65/80", inline=True)
        embed.add_field(name="青菜豆腐湯類", value="55/70", inline=True)
        embed.add_field(name="清湯麺", value="50/65", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飯類", style=discord.ButtonStyle.secondary)
    async def button_rice_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飯類 (加飯+10)",
            color=discord.Color.random()
        )
        embed.add_field(name="羊肉蓋飯", value="120", inline=True)
        embed.add_field(name="酸辣鱿魚蓋飯", value="95", inline=True)
        embed.add_field(name="雞絲蓋飯", value="85", inline=True)
        embed.add_field(name="蒜泥白肉蓋飯", value="85", inline=True)
        embed.add_field(name="酸辣肉片蓋飯", value="85", inline=True)
        embed.add_field(name="蔥油肉片蓋飯", value="85", inline=True)
        embed.add_field(name="蔥油雞絲蓋飯", value="85", inline=True)
        embed.add_field(name="咖哩肉燥蓋飯", value="85", inline=True)
        embed.add_field(name="雞肉絲飯", value="40", inline=True)
        embed.add_field(name="咖哩肉燥飯", value="40", inline=True)
        embed.add_field(name="雞汁飯", value="25", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="麵類", style=discord.ButtonStyle.secondary)
    async def button_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="羊肉拌麺", value="95/115", inline=True)
        embed.add_field(name="酸辣魷魚拌麵", value="80/95", inline=True)
        embed.add_field(name="蒜泥白肉拌類", value="70/85", inline=True)
        embed.add_field(name="酸辣肉片拌麵", value="70/85", inline=True)
        embed.add_field(name="蔥油肉片拌麺", value="70/85", inline=True)
        embed.add_field(name="蔥油雞絲拌麵", value="70/85", inline=True)
        embed.add_field(name="雞肉絲乾麺", value="65/80", inline=True)
        embed.add_field(name="咖哩肉燥乾麺", value="65/80", inline=True)
        embed.add_field(name="雞汁麺", value="50/65", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯類", style=discord.ButtonStyle.secondary)
    async def button_soups(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯類",
            color=discord.Color.random()
        )
        embed.add_field(name="薑絲肉片湯", value="50", inline=True)
        embed.add_field(name="貢丸湯", value="40", inline=True)
        embed.add_field(name="青菜豆腐湯", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="小菜類", style=discord.ButtonStyle.secondary)
    async def button_side_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="小菜類",
            color=discord.Color.random()
        )
        embed.add_field(name="酸辣鱿魚", value="50", inline=True)
        embed.add_field(name="酸辣肉片", value="50", inline=True)
        embed.add_field(name="蒜泥肉片", value="50", inline=True)
        embed.add_field(name="葱油肉片", value="50", inline=True)
        embed.add_field(name="燙青菜", value="40", inline=True)
        embed.add_field(name="皮蛋豆腐", value="40", inline=True)
        embed.add_field(name="豆海滷", value="40", inline=True)
        embed.add_field(name="豆 腐", value="20", inline=True)
        embed.add_field(name="皮 蛋", value="20", inline=True)
        embed.add_field(name="豆 干", value="15", inline=True)
        embed.add_field(name="海 帶", value="15", inline=True)
        embed.add_field(name="油 蛋", value="15", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


        


class Vietnamese_Food(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text="更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="湯麵麵", style=ButtonStyle.secondary)
    async def button_soup_noodles(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="湯麵麵",            
            description="可選 河粉/米粉/麵",
            color=discord.Color.random()
        )
        embed.add_field(name="豬肉/雞肉", value="100", inline=True)
        embed.add_field(name="牛肉片", value="110", inline=True)
        embed.add_field(name="牛肉丸", value="110", inline=True)
        embed.add_field(name="牛腱", value="110", inline=True)
        embed.add_field(name="綜合牛肉", value="130", inline=True)
        embed.add_field(name="海鮮", value="120", inline=True)
        embed.add_field(name="猪腳", value="100", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="酸辣湯麺", style=ButtonStyle.secondary)
    async def button_sour_spicy_soup_noodles(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="酸辣湯麺 ",
            description="可選 河粉/米粉/麵",
            color=discord.Color.random()
        )
        embed.add_field(name="酸辣豬肉/雞肉", value="110", inline=True)
        embed.add_field(name="酸辣牛肉片", value="120", inline=True)
        embed.add_field(name="酸辣牛肉丸", value="120", inline=True)
        embed.add_field(name="酸辣牛腱", value="120", inline=True)
        embed.add_field(name="酸辣綜合牛肉", value="140", inline=True)
        embed.add_field(name="酸辣海鮮", value="120", inline=True)
        embed.add_field(name="酸辣鮮蝦", value="120", inline=True)
        embed.add_field(name="酸辣魚", value="120", inline=True)
        embed.add_field(name="酸辣豬腳", value="110", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="乾拌麵", style=ButtonStyle.secondary)
    async def button_dry_noodles(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="乾拌麵 ",
            description="可選 河粉/米粉",
            color=discord.Color.random()
        )
        embed.add_field(name="乾拌蔬菜", value="70", inline=True)
        embed.add_field(name="乾拌豬肉/雞肉", value="100", inline=True)
        embed.add_field(name="乾拌火腿", value="100", inline=True)
        embed.add_field(name="乾拌排骨", value="100", inline=True)
        embed.add_field(name="乾拌雞腿", value="110", inline=True)
        embed.add_field(name="乾拌鮮蝦", value="110", inline=True)
        embed.add_field(name="乾拌牛肉", value="120", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="炒飯/麵", style=ButtonStyle.secondary)
    async def button_fried_rice_noodles(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="炒飯/麵",
            color=discord.Color.random()
        )
        embed.add_field(name="豬肉炒飯", value="90", inline=True)
        embed.add_field(name="牛肉炒飯", value="100", inline=True)
        embed.add_field(name="蝦仁炒飯", value="110", inline=True)
        embed.add_field(name="海鮮炒飯", value="110", inline=True)
        embed.add_field(name="魚炒飯", value="100", inline=True)
        embed.add_field(name="豬肉炒河粉", value="100", inline=True)
        embed.add_field(name="牛肉炒河粉", value="100", inline=True)
        embed.add_field(name="海鮮炒河粉", value="110", inline=True)
        embed.add_field(name="炒泡麺 海鮮/牛肉/豬肉", value="90", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯麵", style=ButtonStyle.secondary)
    async def button_soups(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="湯麵",
            color=discord.Color.random()
        )
        embed.add_field(name="貢丸湯", value="40", inline=True)
        embed.add_field(name="清湯牛肉湯", value="70", inline=True)
        embed.add_field(name="清湯牛肉丸湯", value="70", inline=True)
        embed.add_field(name="清湯海鮮湯", value="70", inline=True)
        embed.add_field(name="酸辣魚湯", value="80", inline=True)
        embed.add_field(name="酸辣牛肉湯", value="80", inline=True)
        embed.add_field(name="酸辣牛肉丸湯", value="80", inline=True)
        embed.add_field(name="酸辣海鮮湯", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飯類", style=ButtonStyle.secondary)
    async def button_rice_dishes(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="飯類",
            color=discord.Color.random()
        )
        embed.add_field(name="排骨飯", value="110", inline=True)
        embed.add_field(name="雞腿飯", value="120", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="越式小菜", style=ButtonStyle.secondary)
    async def button_vietnamese_sides(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="越式小菜",
            color=discord.Color.random()
        )
        embed.add_field(name="炸春捲(三捲)", value="100", inline=True)
        embed.add_field(name="涼拌春捲(三捲)", value="100", inline=True)
        embed.add_field(name="涼拌木瓜絲", value="70", inline=True)
        embed.add_field(name="果凍火腿", value="60", inline=True)
        embed.add_field(name="越式火腿", value="60", inline=True)
        embed.add_field(name="單點排骨", value="70", inline=True)
        embed.add_field(name="單點雞腿", value="80", inline=True)
        embed.add_field(name="燙青菜", value="40", inline=True)
        embed.add_field(name="越式法國麺包 招牌", value="100", inline=True)
        embed.add_field(name="越式法國麺包 雞肉/豬肉", value="120", inline=True)
        
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)



class Don_Rice(View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text="更新時間:2023/8/21")
        return embed

    @discord.ui.button(label="鍋燒意麵", style=ButtonStyle.secondary)
    async def button_pot_burned_noodles(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="鍋燒意麵",
            color=discord.Color.random()
        )
        embed.add_field(name="昆布鍋燒", value="80", inline=True)
        embed.add_field(name="沙茶鍋燒", value="85", inline=True)
        embed.add_field(name="泡菜鍋燒", value="90", inline=True)
        embed.add_field(name="麻辣鍋燒", value="90", inline=True)
        embed.add_field(name="咖哩鍋燒", value="95", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="炒麵", style=ButtonStyle.secondary)
    async def button_stir_fried_noodles(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="炒麵",
            color=discord.Color.random()
        )
        embed.add_field(name="日式炒麵", value="85", inline=True)
        embed.add_field(name="豬肉炒麵", value="110", inline=True)
        embed.add_field(name="雞肉炒麵", value="115", inline=True)
        embed.add_field(name="鮮菇炒麵", value="100", inline=True)
        embed.add_field(name="牛肉炒麵", value="135", inline=True)
        embed.add_field(name="芥末炒麵", value="85", inline=True)
        embed.add_field(name="胡麻炒麵", value="95", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="丼飯", style=ButtonStyle.secondary)
    async def button_rice_bowls(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="丼飯",
            color=discord.Color.random()
        )
        embed.add_field(name="骰子牛肉丼飯", value="135", inline=True)
        embed.add_field(name="日式親子丼飯", value="90", inline=True)
        embed.add_field(name="日式燒肉丼飯", value="85", inline=True)
        embed.add_field(name="日式牛肉丼飯", value="110", inline=True)
        embed.add_field(name="日式鯛魚丼飯", value="100", inline=True)
        embed.add_field(name="日式鮮菇丼飯(可素)", value="80", inline=True)
        embed.add_field(name="咖哩親子丼飯", value="95", inline=True)
        embed.add_field(name="咖哩燒肉丼飯", value="90", inline=True)
        embed.add_field(name="咖哩牛肉丼飯", value="115", inline=True)
        embed.add_field(name="咖哩鯛魚丼飯", value="105", inline=True)
        embed.add_field(name="咖哩鮮菇丼飯", value="85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="小菜", style=ButtonStyle.secondary)
    async def button_side_dishes(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="小菜",
            color=discord.Color.random()
        )
        embed.add_field(name="胡麻豆腐", value="40", inline=True)
        embed.add_field(name="泡菜", value="40", inline=True)
        embed.add_field(name="涼拌海帶芽", value="35", inline=True)
        embed.add_field(name="涼拌牛蒡絲", value="35", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="丼飯加料", style=ButtonStyle.secondary)
    async def button_extra_rice_bowl_toppings(self, interaction: Interaction, button: Button):
        embed = Embed(
            title="丼飯加料",
            color=discord.Color.random()
        )
        embed.add_field(name="A. 親子", value="45", inline=True)
        embed.add_field(name="B. 燒肉", value="40", inline=True)
        embed.add_field(name="C. 牛肉", value="60", inline=True)
        embed.add_field(name="D. 鯛魚", value="50", inline=True)
        embed.add_field(name="E. 鮮菇", value="35", inline=True)
        embed.add_field(name="F. 骰牛", value="65", inline=True)
        embed.add_field(name="加飯", value="10", inline=True)
        embed.add_field(name="加熟蛋", value="15", inline=True)
        embed.add_field(name="加温泉蛋", value="25", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)




class Big_Q(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/10/21")
        return embed

    @discord.ui.button(label="湯麵類", style=discord.ButtonStyle.secondary)
    async def button_soup_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="雞湯拉麵", value="120", inline=True)
        embed.add_field(name="牛肉麵", value="120", inline=True)
        embed.add_field(name="清燉牛肉麵", value="120", inline=True)
        embed.add_field(name="牛肉湯麵", value="55", inline=True)
        embed.add_field(name="肉燥濕麵", value="55", inline=True)
        embed.add_field(name="清湯麵", value="50", inline=True)
        embed.add_field(name="餛飩麵", value="75", inline=True)
        embed.add_field(name="豬肉麵", value="80", inline=True)
        embed.add_field(name="泡菜豬肉麵", value="95", inline=True)
        embed.add_field(name="沙茶豬肉麵", value="95", inline=True)
        embed.add_field(name="麻辣豬肉麵", value="95", inline=True)
        embed.add_field(name="紅湯抄手", value="75", inline=True)
        embed.add_field(name="蛤蜊麵", value="90", inline=True)
        embed.add_field(name="溫體白肉", value="85", inline=True)
        embed.add_field(name="酸菜白肉麵", value="95", inline=True)
        embed.add_field(name="白肉+蛤蜊", value="120", inline=True)
        embed.add_field(name="牛肉湯餃", value="70 / 90 / 110", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="乾麵類", style=discord.ButtonStyle.secondary)
    async def button_dry_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="乾麵類",
            color=discord.Color.random()
        )
        embed.add_field(name="牛肉乾拌麵", value="100 / 110 / 120", inline=True)
        embed.add_field(name="大Q麵", value="45 / 60 / 75", inline=True)
        embed.add_field(name="月見麵", value="60 / 75 / 90", inline=True)
        embed.add_field(name="乾擔仔麵", value="40 / 65", inline=True)
        embed.add_field(name="乾陽春輝", value="40 / 65", inline=True)
        embed.add_field(name="手工乾意麵", value="40 / 60 / 65", inline=True)
        embed.add_field(name="乾粿仔條", value="40 / 60 / 65", inline=True)
        embed.add_field(name="乾細拉麵", value="40 / 60 / 65", inline=True)
        embed.add_field(name="麻辣乾麵", value="45 / 60 / 70", inline=True)
        embed.add_field(name="沙茶麺", value="45 / 60 / 70", inline=True)
        embed.add_field(name="麻醬麺(可素)", value="45 / 60 / 70", inline=True)
        embed.add_field(name="肉燥麻醬麵", value="50 / 65 / 75", inline=True)
        embed.add_field(name="醡醬麵", value="45 / 60 / 70", inline=True)
        embed.add_field(name="特製醡麻麵", value="50 / 65 / 75", inline=True)
        embed.add_field(name="紅油抄手麵2.0", value="70 / 75 / 90", inline=True)
        embed.add_field(name="紅油抄手麵", value="70 / 75 / 90", inline=True)
        embed.add_field(name="抄手麵(不辣)", value="65 / 75 / 85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯類", style=discord.ButtonStyle.secondary)
    async def button_soups(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯類",
            color=discord.Color.random()
        )
        embed.add_field(name="油豆腐湯", value="25", inline=True)
        embed.add_field(name="蛋花湯", value="30", inline=True)
        embed.add_field(name="手工貢丸湯", value="30", inline=True)
        embed.add_field(name="虱目魚丸湯", value="30", inline=True)
        embed.add_field(name="青菜湯", value="30", inline=True)
        embed.add_field(name="醌純湯", value="40", inline=True)
        embed.add_field(name="牛肉湯蛋花", value="40", inline=True)
        embed.add_field(name="貢丸蛋花湯", value="45", inline=True)
        embed.add_field(name="青菜蛋花湯", value="45", inline=True)
        embed.add_field(name="白肉湯", value="45", inline=True)
        embed.add_field(name="嘴邊肉湯", value="45", inline=True)
        embed.add_field(name="蛤蜊湯", value="50", inline=True)
        embed.add_field(name="牛肉湯", value="85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飯蓋飯類", style=discord.ButtonStyle.secondary)
    async def button_rice_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飯蓋飯類",
            color=discord.Color.random()
        )
        embed.add_field(name="肉燥飯", value="30 / 40 / 50", inline=True)
        embed.add_field(name="酔醬飯", value="30 / 40 / 50", inline=True)
        embed.add_field(name="旗魚酥飯", value="40 / 50 / 60", inline=True)
        embed.add_field(name="牛肉湯泡飯", value="50 / 60 / 70", inline=True)
        embed.add_field(name="大Q白肉蓋飯", value="80", inline=True)
        embed.add_field(name="雞胸肉蓋飯", value="100", inline=True)
        embed.add_field(name="牛肉蓋飯", value="120", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="小菜類", style=discord.ButtonStyle.secondary)
    async def button_side_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="小菜類",
            color=discord.Color.random()
        )
        embed.add_field(name="水餃(高麗/韭)", value="5.5", inline=True)
        embed.add_field(name="鲁貢丸2顆", value="15", inline=True)
        embed.add_field(name="滷蛋", value="15", inline=True)
        embed.add_field(name="溏心蛋", value="20", inline=True)
        embed.add_field(name="豆干", value="20", inline=True)
        embed.add_field(name="乾油豆腐", value="20", inline=True)
        embed.add_field(name="燙青菜(時蔬)", value="30", inline=True)
        embed.add_field(name="燙地瓜葉", value="30", inline=True)
        embed.add_field(name="燙豆芽菜", value="30", inline=True)
        embed.add_field(name="煙燻豬頭皮", value="30", inline=True)
        embed.add_field(name="皮蛋豆腐", value="40", inline=True)
        embed.add_field(name="紅油抄手", value="50", inline=True)
        embed.add_field(name="白油抄手", value="50", inline=True)
        embed.add_field(name="乾嘴邊肉", value="50", inline=True)
        embed.add_field(name="蒜泥白肉", value="50", inline=True)
        embed.add_field(name="雞胸肉", value="55", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)




class U_Pin(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2023/10/21")
        return embed

    @discord.ui.button(label="廣東粥", style=discord.ButtonStyle.secondary)
    async def button_congee(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="廣東粥",
            color=discord.Color.random()
        )
        embed.add_field(name="牛肉粥", value="85", inline=True)
        embed.add_field(name="禦品招牌粥", value="85", inline=True)
        embed.add_field(name="鮑魚粥", value="85", inline=True)
        embed.add_field(name="魚片粥", value="85", inline=True)
        embed.add_field(name="蝦仁瘦肉粥", value="85", inline=True)
        embed.add_field(name="花枝瘦肉粥", value="80", inline=True)
        embed.add_field(name="吻仔魚粥", value="80", inline=True)
        embed.add_field(name="海鮮粥", value="80", inline=True)
        embed.add_field(name="廣東粥", value="80", inline=True)
        embed.add_field(name="香菇瘦肉粥", value="80", inline=True)
        embed.add_field(name="玉米瘦肉粥", value="75", inline=True)
        embed.add_field(name="皮蛋瘦肉粥", value="75", inline=True)
        embed.add_field(name="鹹蛋瘦肉粥", value="75", inline=True)
        embed.add_field(name="豬肝瘦肉粥", value="75", inline=True)
        embed.add_field(name="蔬菜粥", value="75", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="海鮮鍋燒麵(湯)", style=discord.ButtonStyle.secondary)
    async def button_seafood_noodles_soup(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="海鮮鍋燒麵(湯)",
            color=discord.Color.random()
        )
        embed.add_field(name="烏龍麵", value="90", inline=True)
        embed.add_field(name="意麵", value="90", inline=True)
        embed.add_field(name="拉麵", value="90", inline=True)
        embed.add_field(name="冬粉", value="90", inline=True)
        embed.add_field(name="米粉", value="90", inline=True)
        embed.add_field(name="粄條", value="90", inline=True)
        embed.add_field(name="雞絲麵", value="90", inline=True)
        embed.add_field(name="菜蛋麵", value="60", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="日式炒麵(乾)", style=discord.ButtonStyle.secondary)
    async def button_japanese_fried_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="日式炒麵(乾)",
            color=discord.Color.random()
        )
        embed.add_field(name="烏龍麵", value="90", inline=True)
        embed.add_field(name="意麵", value="90", inline=True)
        embed.add_field(name="拉麵", value="90", inline=True)
        embed.add_field(name="粄條", value="90", inline=True)
        embed.add_field(name="雞絲麵", value="90", inline=True)
        embed.add_field(name="菜肉麵", value="65", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class Big_Water_Fire(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/08/10")
        return embed

    @discord.ui.button(label="大夶𡘙炒飯", style=discord.ButtonStyle.secondary)
    async def button_fried_rice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="大夶𡘙炒飯",
            color=discord.Color.random()
        )
        embed.add_field(name="雙蛋蛋蒽炒飯", value="80", inline=True)
        embed.add_field(name="肉絲炒飯", value="80", inline=True)
        embed.add_field(name="蝦仁炒飯", value="80", inline=True)
        embed.add_field(name="牛肉炒飯", value="80", inline=True)
        embed.add_field(name="雞丁炒飯", value="80", inline=True)
        embed.add_field(name="香腸炒飯", value="80", inline=True)
        embed.add_field(name="鮭魚炒飯", value="100", inline=True)
        embed.add_field(name="總匯牛炒飯", value="130(牛+香腸+蝦)", inline=True)
        embed.add_field(name="總匯豬炒飯", value="130(豬+香腸+蝦)", inline=True)
        embed.add_field(name="大夶猋香腸炒飯", value="200(大香腸)(限量)", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="水沝淼水煮餐", style=discord.ButtonStyle.secondary)
    async def button_boiled_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="水沝淼水煮餐",
            description="""ロ味為味噌胡麻醬、和風照燒醬、椒鹽,三選一
主食餐點皆可調整飯量
内含高麗菜、菠菜、杏鮑菇、玉米筍""",
            color=discord.Color.random()
        )
        embed.add_field(name="舒肥雞肉餐", value="100", inline=True)
        embed.add_field(name="舒肥大肌肌餐", value="100", inline=True)
        embed.add_field(name="水煮多利魚餐", value="120", inline=True)
        embed.add_field(name="水煮豬肉餐", value="100", inline=True)
        embed.add_field(name="豬多多餐", value="100", inline=True)
        embed.add_field(name="水煮素食餐", value="100", inline=True)
        embed.add_field(name="水煮牛肉餐", value="100", inline=True)
        embed.add_field(name="牛多多餐", value="100", inline=True)
        embed.add_field(name="小仙女餐", value="60", inline=True)
       
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="水沝淼加點區", style=discord.ButtonStyle.secondary)
    async def button_boiled_meals(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="水沝淼加點區",
            description="""不可單點須點水沝淼主餐""",
            color=discord.Color.random()
        )
        
        embed.add_field(name="溏溏溏心蛋(一粒)", value="15", inline=True)
        embed.add_field(name="純愛雞胸", value="40", inline=True)
        embed.add_field(name="真的鮮白蝦(五隻)", value="50", inline=True)
        embed.add_field(name="豬肉來一份", value="40", inline=True)
        embed.add_field(name="好吃蔬菜", value="30", inline=True)
        embed.add_field(name="一份牛肉", value="40", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


    @discord.ui.button(label="火炎焱單主食丼飯", style=discord.ButtonStyle.secondary)
    async def button_charcoal_donburi(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="火炎焱單主食丼飯",
            description="""丼飯皆附碳烤食蔬(親子丼除外)
            +牛/豬肉(2.5oz) 40 + 起司 15 + 溫玉 15 + 蔥 10
""",
            color=discord.Color.random()
        )
        embed.add_field(name="炭燒牛五花丼", value="100", inline=True)
        embed.add_field(name="炭燒豬五花丼", value="100", inline=True)
        embed.add_field(name="炭燒起司親子丼", value="100", inline=True)
        embed.add_field(name="炭燒烤蝦丼", value="100", inline=True)
        embed.add_field(name="炭燒鯖魚丼", value="100", inline=True)
        embed.add_field(name="炭燒雞腿丼", value="110", inline=True)
        embed.add_field(name="炭燒鮭魚丼", value="150", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="火炎焱雙主食丼飯", style=discord.ButtonStyle.secondary)
    async def button_double_charcoal_donburi(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="火炎焱雙主食丼飯",
            description="""丼飯皆附碳烤食蔬(親子丼除外)
            +牛/豬肉(2.5oz) 40 + 起司 15 + 溫玉 15 + 蔥 10
""",
            color=discord.Color.random()
        )
        embed.add_field(name="炭燒牛五花丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒牛五花丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒豬五花丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒豬五花丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒純牛丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒純牛丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒純豬丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒純豬丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒起司親子丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒起司親子丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒烤蝦丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒烤蝦丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒鯖魚丼+魚", value="140", inline=True)
        embed.add_field(name="炭燒鯖魚丼+蝦", value="140", inline=True)
        embed.add_field(name="炭燒雞腿丼+魚", value="150", inline=True)
        embed.add_field(name="炭燒雞腿丼+蝦", value="150", inline=True)
        embed.add_field(name="炭燒鮭魚丼+魚", value="190", inline=True)
        embed.add_field(name="炭燒鮭魚丼+蝦", value="190", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="火炎焱單點", style=discord.ButtonStyle.secondary)
    async def button_charcoal_single(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="火炎焱單點",
            color=discord.Color.random()
        )
        embed.add_field(name="炭烤時蔬", value="30", inline=True)
        embed.add_field(name="炭烤白蝦", value="50", inline=True)
        embed.add_field(name="炭烤雞腿(4oz)", value="45", inline=True)
        embed.add_field(name="炭烤鯖魚(半尾)", value="50", inline=True)
        embed.add_field(name="炭烤鮭魚(2oz)", value="50", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class Yummy_Rice(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/08/10")
        return embed

    @discord.ui.button(label="炒飯", style=discord.ButtonStyle.secondary)
    async def button_fried_rice(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="炒飯",
            color=discord.Color.random()
        )
        embed.add_field(name="沙茶羊肉蛋炒飯", value="100", inline=True)
        embed.add_field(name="鳳梨蝦仁蛋炒飯", value="100", inline=True)
        embed.add_field(name="玉米蛋炒飯", value="70", inline=True)
        embed.add_field(name="豬肉蛋炒飯", value="80", inline=True)
        embed.add_field(name="牛肉蛋炒飯", value="85", inline=True)
        embed.add_field(name="蝦仁蛋炒飯", value="85", inline=True)
        embed.add_field(name="鮭魚蛋炒飯", value="90", inline=True)
        embed.add_field(name="鹹豬肉炒飯", value="90", inline=True)
        embed.add_field(name="德式香腸蛋炒飯", value="85", inline=True)
        embed.add_field(name="塔香雞肉蛋炒飯", value="85", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="湯", style=discord.ButtonStyle.secondary)
    async def button_soup(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="湯",
            color=discord.Color.random()
        )
        embed.add_field(name="虱目魚丸湯", value="35", inline=True)
        embed.add_field(name="紫菜蛋花湯", value="35", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

class Brother_Rice_Ball(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/08/10")
        return embed

    @discord.ui.button(label="飯糰", style=discord.ButtonStyle.secondary)
    async def button_rice_balls(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飯糰",
            color=discord.Color.random()
        )
        embed.add_field(name="糖心蛋飯糰", value="50", inline=True)
        embed.add_field(name="泡菜海台飯糰", value="55", inline=True)
        embed.add_field(name="德式香腸飯糰", value="55", inline=True)
        embed.add_field(name="起司鮪魚飯糰", value="55", inline=True)
        embed.add_field(name="煙燻G肉飯糰", value="55", inline=True)
        embed.add_field(name="德州烤腿排飯糰", value="60", inline=True)
        embed.add_field(name="椒麻G腿排飯糰", value="60", inline=True)
        embed.add_field(name="H素飯糰", value="50", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飲料", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            color=discord.Color.random()
        )
        embed.add_field(name="豆漿紅茶", value="25", inline=True)
        embed.add_field(name="鮮奶茶", value="30", inline=True)
        embed.add_field(name="紅茶", value="20", inline=True)
        embed.add_field(name="豆漿", value="25", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


class Big_Red(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/08/10")
        return embed

    @discord.ui.button(label="抄手/麵", style=discord.ButtonStyle.secondary)
    async def button_wontons_noodles(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="抄手/麵",
            color=discord.Color.random()
        )
        embed.add_field(name="白油抄手", value="50", inline=True)
        embed.add_field(name="白油抄手麵", value="80", inline=True)
        embed.add_field(name="原湯抄手", value="50", inline=True)
        embed.add_field(name="原湯抄手麵", value="75", inline=True)
        embed.add_field(name="紅油抄手", value="50", inline=True)
        embed.add_field(name="紅油抄手麵", value="80", inline=True)
        embed.add_field(name="酸辣抄手", value="50", inline=True)
        embed.add_field(name="酸辣抄手麵", value="80", inline=True)
        embed.add_field(name="白油燃麵", value="50", inline=True)
        embed.add_field(name="原湯少年", value="50", inline=True)
        embed.add_field(name="紅油燃麵", value="50", inline=True)
        embed.add_field(name="酸辣麵", value="60", inline=True)
        embed.add_field(name="擔擔麵", value="60", inline=True)
        embed.add_field(name="榨菜肉絲麵", value="70", inline=True)
        embed.add_field(name="八寶炸醬麵", value="70", inline=True)
        embed.add_field(name="酸辣榨菜肉絲麵", value="75", inline=True)
        embed.add_field(name="牛肉碎末麵", value="75", inline=True)
        embed.add_field(name="牛肉湯麵+抄手", value="80", inline=True)
        embed.add_field(name="酸辣牛肉碎末麵", value="80", inline=True)
        embed.add_field(name="雙牛拌麵", value="120", inline=True)
        embed.add_field(name="酸辣雙牛拌麵", value="120", inline=True)
        embed.add_field(name="牛肉湯麵", value="60", inline=True)
        embed.add_field(name="大紅袍牛肉麵", value="120", inline=True)
        embed.add_field(name="雙牛湯麵", value="135", inline=True)
        embed.add_field(name="導演麵", value="80", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

class Korean_Cuisine(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/08/10")
        return embed

    @discord.ui.button(label="韓式料理", style=discord.ButtonStyle.secondary)
    async def button_korean_food(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed1 = discord.Embed(
            title="韓式料理",
            color=discord.Color.random()
        )
        embed1.add_field(name="韓式拌飯(牛、豬)", value="130", inline=True)
        embed1.add_field(name="韓式石頭鍋拌飯(牛、豬)", value="150", inline=True)
        embed1.add_field(name="韓式米勺鍋飯(大中小辣)", value="150", inline=True)
        embed1.add_field(name="韓式泡菜鍋飯", value="150", inline=True)
        embed1.add_field(name="韓式豆腐鍋飯", value="150", inline=True)
        embed1.add_field(name="韓式烤肉飯(牛、豬)", value="150", inline=True)
        embed1.add_field(name="韓式部隊鍋飯(一人份)(拉、冬)", value="180", inline=True)
        embed1.add_field(name="韓式部隊鍋飯(二人份)(拉、冬)", value="340", inline=True)
        embed1.add_field(name="韓式豬軟骨湯飯", value="150", inline=True)
        embed1.add_field(name="甜辣雞飯", value="150", inline=True)
        embed1.add_field(name="孜然排骨飯", value="170", inline=True)
        embed1.add_field(name="單點煎鯖魚", value="100", inline=True)
        embed1.add_field(name="煎鯖魚套餐", value="150", inline=True)
        embed1.add_field(name="韓式拳頭飯糰", value="150", inline=True)
        embed1.add_field(name="韓式炒碼麵/飯", value="130", inline=True)
        embed1 = self.add_footer(embed1)

        embed2 = discord.Embed(
            title="韓式料理",
            color=discord.Color.random()
        )
        embed2.add_field(name="韓式炸醬麵/飯", value="130", inline=True)
        embed2.add_field(name="韓式辛拉麵起司/泡菜", value="100", inline=True)
        embed2.add_field(name="韓式年糕湯(牛)", value="150", inline=True)
        embed2.add_field(name="韓式辣炒年糕", value="150", inline=True)
        embed2.add_field(name="韓式海鮮煎餅", value="150", inline=True)
        embed2.add_field(name="韓式糖醋肉", value="350", inline=True)
        embed2.add_field(name="韓式乾烹肉(雞)", value="350", inline=True)
        embed2.add_field(name="孜然排骨", value="350", inline=True)
        embed2.add_field(name="韓式蔘雞湯(需預訂)", value="500", inline=True)
        embed2.add_field(name="白飯", value="10", inline=True)
        embed2.add_field(name="小菜外帶(盒裝)", value="40", inline=True)
        embed2.add_field(name="泡菜外帶(罐裝)", value="150", inline=True)
        embed2 = self.add_footer(embed2)

        await interaction.response.edit_message(embeds=[embed1, embed2])


class Grandma_Sushi(discord.ui.View):
    def __init__(self):
        super().__init__()

    def add_footer(self, embed):
        embed.set_footer(text=f"更新時間:2024/08/10")
        return embed

    @discord.ui.button(label="主食", style=discord.ButtonStyle.secondary)
    async def button_main_dishes(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="主食",
            color=discord.Color.random()
        )
        embed.add_field(name="飯丸", value="45", inline=True)
        embed.add_field(name="壽司", value="35", inline=True)
        embed.add_field(name="炒麵", value="35", inline=True)
        embed.add_field(name="茶碗蒸", value="35", inline=True)
        embed.add_field(name="滷肉飯", value="35", inline=True)
        embed.add_field(name="味噌魚丸", value="35", inline=True)
        embed.add_field(name="味噌泡飯", value="45", inline=True)
        embed.add_field(name="原味咖哩飯", value="70", inline=True)
        embed.add_field(name="雞排咖哩飯", value="90", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="飲料", style=discord.ButtonStyle.secondary)
    async def button_drinks(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="飲料",
            color=discord.Color.random()
        )
        embed.add_field(name="豆漿紅茶", value="20", inline=True)
        embed.add_field(name="伯爵紅茶", value="20", inline=True)
        embed.add_field(name="豆漿", value="20", inline=True)
        embed.add_field(name="伯爵鮮奶茶", value="30", inline=True)
        embed.add_field(name="西瓜汁", value="35", inline=True)
        embed.add_field(name="味噌湯", value="20", inline=True)
        embed.add_field(name="西瓜牛奶", value="45", inline=True)
        embed = self.add_footer(embed)
        await interaction.response.edit_message(embed=embed)


