import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types

from settings import credentials

token = credentials.telegram_token
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", datefmt="%y-%m-%d %H:%M:%S"
)
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def handle_start(message: types.Message) -> None:
    await message.answer("Привет, ты в боте!")


@dp.message_handler()
async def handle_message(message: types.Message) -> None:
    try:
        amount = int(message.text)
    except ValueError:
        await message.reply(f"<b>Error</b>, not a number: {message.text}", parse_mode="html")
    else:
        sleep_message = await message.answer(f"Awaiting for {amount} seconds")
        # time.sleep(1)
        await asyncio.sleep(1)
        for i in range(amount - 1, 0, -1):
            await sleep_message.edit_text(f"Awaiting for {i} seconds")
            # time.sleep(1)
            await asyncio.sleep(1)
        await sleep_message.edit_text(f"Waiting for {amount} seconds is done!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
