# Insta Video Downloader Bot

This is a Telegram bot that downloads Instagram videos using `yt-dlp` and sends them to users.

## Features
- Automatically detects Instagram video links.
- Downloads videos in the best MP4 format.
- Sends the downloaded video back to the user.
- Handles errors and invalid links.
- Uses `yt-dlp` for high-speed downloading with retries.

## Requirements
- Python 3.x
- `telepot` library
- `yt-dlp` library

## Installation

1. Install dependencies:
   ```sh
   pip install telepot yt-dlp
   ```

2. Set up your bot:
   - Create a Telegram bot using [BotFather](https://t.me/BotFather) and obtain your bot token.
   - Replace `TOKEN = ""` in the script with your actual bot token.

3. Run the bot:
   ```sh
   python Insta-Video-Downloader-Bot.py
   ```

## Usage
- Send an Instagram video link to the bot.
- The bot will process the link and download the video.
- The bot will send the downloaded video back to you.

## Security Considerations
- **Do not expose your bot token**: Keep your bot token private and do not share it in public repositories.
- **Use environment variables**: Instead of hardcoding the token, use environment variables for better security.
- **Validate user input**: Ensure the bot only processes valid Instagram URLs to prevent abuse.
- **Rate limiting**: Implement rate limiting to prevent spamming and excessive usage.
- **Use a secure server**: If deploying on a server, ensure it's properly secured with firewalls and updated packages.

## Notes
- Ensure that the bot has permission to send videos.
- This bot works only with public Instagram videos.

## License
This project is licensed under the MIT License.

