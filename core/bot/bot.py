import asyncio
from aiogram import Bot, Dispatcher
from core.config.config import Config as config
from core.logg.logger import set_logger

logger = set_logger('bot')
logger.info('START BOT LOGGING')

async def assert_start(bot: Bot) -> None:
    """
    Отправляет команду на установку команд бота и сообщение об запуске бота администратору.

    Arguments:
        bot (Bot): Инстанс бота.
    """
    logger.debug('Bot started')
    await bot.send_message(config.ADMIN_ID, 'Бот запущен')

async def assert_stop(bot: Bot) -> None:
    """
    Отправляет сообщение об остановке бота администратору.

    Arguments:
        bot (Bot): Инстанс бота.
    """
    logger.debug('Bot stopped')
    await bot.send_message(config.ADMIN_ID, 'Бот остановлен')


async def handle_bot_operations() -> None:
    """
    Обрабатывает операции с ботом, в данном случае - отслеживание запуска и остановки бота.
    """
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()
    logger.debug('bot and dispatcher created')
    dp.startup.register(assert_start)
    dp.shutdown.register(assert_stop)
    try:
        logger.debug('Start polling')
        await dp.start_polling(bot, polling_timeout=15, бskip_updates=True)
    except Exception as ex:
        logger.exception(ex)
    finally:
        logger.debug('Bot session closed')
        await bot.session.close()


async def main() -> None:
    """
    Главная функция, инициализирующая обработку операций с ботом.
    """
    task_bot = asyncio.create_task(handle_bot_operations())
    await task_bot

if __name__ == '__main__':
    asyncio.run(main())