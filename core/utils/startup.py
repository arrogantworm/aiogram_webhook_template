from aiogram import Router, Bot
from core.settings import config


router = Router()


@router.startup()
async def on_startup(bot: Bot):
    await bot.send_message(chat_id=config.ADMIN_ID, text='Бот запущен')


@router.shutdown()
async def on_shutdown(bot: Bot):
    await bot.send_message(chat_id=config.ADMIN_ID, text='Бот остановлен')
