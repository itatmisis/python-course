import logging
import time
import asyncio

from aiogram import Bot, Dispatcher, executor, types, utils

token = ''
logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%y-%m-%d %H:%M:%S')
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    try:
        amount = int(message.text)
    except ValueError:
        await message.reply(f'<b>Error</b>, not a number: {message.text}', parse_mode='html')
    else:
        sleep_message = await message.answer(f'Awaiting for {amount} seconds')
        await asyncio.sleep(1)
        for i in range(amount-1, 0, -1):
            await sleep_message.edit_text(f'Awaiting for {i} seconds')
            await asyncio.sleep(1)
        await sleep_message.edit_text(f'Waiting for {amount} seconds done!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)