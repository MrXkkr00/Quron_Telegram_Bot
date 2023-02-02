# https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu
import types
#
# from joblib import executor
from sphinx.util import requests
# #
# sura=1
# oyat=3
# url=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json'
#
# response=requests.get(url)
# print(response.json()['text'])
# # print(response.json())
# res=response.json()
# # print(res)
# print(res['conversion_rate'])
#
#
# """
# This is a echo bot.
# It echoes any incoming text messages.
# """

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1903749937:AAEI72c2tb3cCE_fyNcvqsFZxhKcP8vkL3s'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!\nBu bot Rasulbek tomonidan yaratildi\nMenda o'zbek tilidagi oyatni topishingiz mumkin\nfoydalanish 1-5 yani 1-sura 5- oyat.")



@dp.message_handler()
async def echo(message: types.Message):
    for i in range(len(message.text) - 1):
        if message.text[i] == '-':
            sura = (message.text[:i])
            oyat = (message.text[i + 1:])


    #
    # sura = int(message.text[0]+message.text[1])
    # oyat = int(message.text[2]+message.text[3])

    url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json'
    response = requests.get(url)



    await message.answer(response.json()['text'])
    # await message.answer(type(sura))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)