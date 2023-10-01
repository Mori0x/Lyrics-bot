# Telegram Song Lyrics Bot

## Overview

This Python bot is designed to be used on the Telegram messaging platform. It has two main functionalities:

1. **Find Lyrics from a Song**
   - Users can send a command `Find lyrics from song` followed by the name of the song they want to find lyrics for.
   - The bot will make a request to the Genius API to search for the lyrics of the provided song and return the lyrics to the user.

2. **Find Song from Lyrics**
   - Users can send a command `Find song from lyrics` followed by a snippet of lyrics from a song.
   - The bot will search the Genius API for songs containing the provided lyrics and return the names of the matching songs to the user.

## Getting Started

### Prerequisites

Before you can use this bot, you will need the following:

- Python 3.x installed on your system.
- Telegram Bot API Token (you can get it from the [BotFather](https://core.telegram.org/bots#botfather)).
- Genius API Token (you can obtain it by signing up for the [Genius API](https://genius.com/api-clients)).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Mori0x/telegram-lyrics-bot.git
   ```
2. Install necessary libraries:
   ```bash
   pip install python-telegram-bot
   ```
   ```bash
   pip install lyricsgenius
   ```
   ```bash
   pip install requests
   ```
3. Run the bot
   ```bash
   python main.py
   ```
## Usage

1. Start a chat with your Telegram bot.
2. Send `Find lyrics from song` followed by the name of the song to get lyrics.
3. Send `Find song from lyrics` followed by a snippet of lyrics to find the song's name.

## Feedback and Contributions

Feel free to contribute to this project by submitting issues or pull requests on GitHub. If you have any feedback or suggestions for improvement, please let us know.

## License

This project is licensed under the [MIT License](https://github.com/Mori0x/telegram-lyrics-bot/blob/master/LICENSE).

## Acknowledgments

- This bot uses the Genius API to retrieve song lyrics. Make sure to check and comply with Genius's terms of use when using their API.

## Author

- Mori0x

## Disclaimer

- This bot is for educational and personal use only. Ensure you comply with Telegram's and Genius's terms of service when using this bot.

## Conclusion

With this README.md file, you can guide users on how to set up and use your Telegram bot for finding song lyrics and songs based on lyrics snippets. Make sure to replace placeholders with your actual API tokens and customize it further to suit your project's needs.
