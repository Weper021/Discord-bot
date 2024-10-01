import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio

# FFmpeg路径
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

ytdl_format_options = {
    'format': 'bestaudio/best',
    'noplaylist': 'True',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

async def setup(bot):
    @bot.command()
    async def play(ctx, url: str):
        if ctx.author.voice is None:
            await ctx.send("你需要先加入一个语音频道。")
            return

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        voice_client = await voice_channel.connect()

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

        audio_source = discord.FFmpegPCMAudio(data['url'], **FFMPEG_OPTIONS)
        voice_client.play(audio_source, after=lambda e: print(f"播放完毕: {e}"))
        await ctx.send(f"正在播放: **{data['title']}**")

    @bot.command()
    async def leave(ctx):
        voice_client = ctx.voice_client
        if voice_client is not None and voice_client.is_connected():
            await voice_client.disconnect()
            await ctx.send("我已离开语音频道。")
        else:
            await ctx.send("我不在任何语音频道里。")
