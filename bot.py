from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from core.settings import config
from aiohttp import web
import asyncio
import logging
from core.handlers import basic


async def on_startup(bot: Bot):
    await bot.send_message(config.ADMIN_ID.get_secret_value(), 'Бот запущен')


async def on_shutdown(bot: Bot):
    await bot.send_message(config.ADMIN_ID.get_secret_value(), 'Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    bot = Bot(config.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # Routers
    dp.include_router(basic.router)

    try:
        await bot.set_webhook(
            url=config.URL_DOMAIN.get_secret_value() + config.URL_PATH.get_secret_value(),
            drop_pending_updates=True,
            allowed_updates=dp.resolve_used_update_types()
        )
        app = web.Application()
        SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=config.URL_PATH.get_secret_value())
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, host=config.SERVER_HOST.get_secret_value(), port=config.SERVER_PORT.get_secret_value())
        await site.start()

        await asyncio.Event().wait()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
