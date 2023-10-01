import telebot
import lyricsgenius
from telebot import types
import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("File .env wasn't found")
else:
    load_dotenv()

bot_token = os.getenv('BOT_TOKEN')


genius_token = os.getenv('GENIUS_KEY')

bot = telebot.TeleBot(bot_token)
genius = lyricsgenius.Genius(genius_token)


@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    bot.reply_to(message, 'Welcome to Lyrics bot! This bot can find lyrics from song title and song title from lyrics.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Find lyrics from song")
    btn2 = types.KeyboardButton('Find song from lyrics')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Choose what i should to do", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def distribution(message):
    if message.text == 'Find lyrics from song':
        bot.send_message(message.from_user.id, 'Send title of song')
        bot.register_next_step_handler(message, get_lyrics)
    elif message.text == 'Find song from lyrics':
        bot.send_message(message.from_user.id, 'Send lyrics of song(without words Verse, Pre-Chorus, Chorus, Bridge etc. Not necessarily full lyrics')
        bot.register_next_step_handler(message, get_title)


@bot.message_handler(func=lambda message: True)
def get_lyrics(message):
    title = message.text.strip()
    song = genius.search_song(title)

    if song:
        lyrics = song.lyrics
        text = text_format(lyrics)
        bot.reply_to(message, text)
    else:
        bot.reply_to(message, 'Can not find song with this name. Check title for correct')


@bot.message_handler(content_types=['text'])
def get_title(message):
    search_results = genius.search_lyrics(message.text)

    if search_results:
        song_title = search_results['sections'][0]['hits'][0]['result']['full_title']
        response = f"I couldn't find the exact song you requested, but I found a song titled {song_title}"
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Sorry, I couldn't find the lyrics or the song you requested.")


def text_format(lyrics):
    fir = lyrics.split(' ')
    sec = ''
    bad_word = False
    for word in fir:
        if 'Lyrics' in word:
            bad_word = True
            sec += f'{word}'
            continue

        if bad_word:
            sec += f' {word}'

    thrd = ''

    res_word = ''

    for word2 in sec.split(' '):
        if word2.isdigit() or 'Embed' in word2:
            for letter in sec.split(' ')[len(sec.split(' ')) - 1]:
                if letter.isdigit():
                    break
                res_word += letter
            thrd += f' {res_word}'
            continue
        thrd += f' {word2}'

    return thrd


bot.polling()