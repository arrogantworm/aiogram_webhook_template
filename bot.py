from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from core.settings import config
from aiohttp import web
import asyncio
import logging
from core.handlers import basic


async def on_startup(bot: Bot, dp: Dispatcher):
    await bot.set_webhook(
        url=config.URL_DOMAIN + config.URL_PATH,
        drop_pending_updates=True,
        allowed_updates=dp.resolve_used_update_types()
    )
    await bot.send_message(config.ADMIN_ID, 'Бот запущен')


async def on_shutdown(bot: Bot):
    await bot.delete_webhook()
    await bot.send_message(config.ADMIN_ID, 'Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    session = AiohttpSession()
    bot_settings = {'session': session, 'parse_mode': 'HTML'}
    bot = Bot(config.BOT_TOKEN.get_secret_value(), **bot_settings)
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Routers
    dp.include_router(basic.router)

    try:

        app = web.Application()
        SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=config.URL_PATH)
        setup_application(app, dp, bot=bot)
        web.run_app(app, host=config.SERVER_HOST, port=config.SERVER_PORT)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
