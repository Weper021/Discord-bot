import os
import openai
from discord.ext import commands

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chat')
    async def chat_command(self, ctx, *, message):
        # 调用 OpenAI API
        response = await self.get_openai_response(message)
        await ctx.send(response)

    async def get_openai_response(self, message):
        # 设置 OpenAI API 密钥
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        # 调用 GPT-4 模型
        try:
            # 这里是新版的调用方式
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            return completion['choices'][0]['message']['content']
        except Exception as e:
            return f"出错了: {str(e)}"

async def setup(bot):
    await bot.add_cog(Chat(bot))
