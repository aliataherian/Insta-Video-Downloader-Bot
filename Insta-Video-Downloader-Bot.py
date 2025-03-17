import telepot
import yt_dlp
import os
import time

TOKEN = ""
bot = telepot.Bot(TOKEN)

def download_instagram_video(url):
    """Download Instagram video"""
    try:
        ydl_opts = {
            'outtmpl': 'video.mp4',
            'format': 'best[ext=mp4]',
            'noprogress': True,
            'retries': 10,
            'fragment-retries': 10,
            'http-chunk-size': '4M',
            'concurrent-fragments': 5,
            'nocheckcertificate': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "video.mp4"
    except Exception as e:
        return str(e)

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg.get('text', '')

    # Check if the message is an Instagram link
    if text.startswith("https://www.instagram.com/"):
        bot.sendMessage(chat_id, "Downloading the video at high speed, please wait...")
        video_file = download_instagram_video(text)

        if os.path.exists(video_file):
            bot.sendVideo(chat_id, open(video_file, "rb"))
            os.remove(video_file)
        else:
            bot.sendMessage(chat_id, f"An error occurred: {video_file}")

    else:
        bot.sendMessage(chat_id, "Please send a valid Instagram link.")

bot.message_loop(handle)

print("The bot is running...")
while True:
    time.sleep(10)
