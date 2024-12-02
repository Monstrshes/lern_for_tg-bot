import asyncio

from config_data.config import Config, load_config
from aiogram import Dispatcher, Bot
from handlers import other_hanlers, user_handlers

async def main() -> None:
    config: Config = load_config() #Загружаем токен

    #инициализируем бота и диспетчер
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher

    #Создаём роутеры
    dp.include_router(other_hanlers.router)
    dp.include_router(user_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())