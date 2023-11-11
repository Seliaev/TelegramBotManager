from dotenv import load_dotenv
import os
import secrets
from core.utils.bot_status import is_bot_running
from core.logg.logger import set_logger

logger = set_logger('config')
logger.info('START CONFIG')

env_file_path = 'core/config/.env'
if not os.path.exists(env_file_path):
    logger.error('There is no .env file. Create it.')
    print('There is no .env file. Create it.')
    exit()
else:
    load_dotenv(dotenv_path=env_file_path)


class Config:
    """
    Класс для хранения конфигурационных параметров бота.

    Arguments:
    - TOKEN (str): Токен бота для подключения к API Telegram.
    - ADMIN_ID (str): Идентификатор администратора бота.
    - PASSWORD (str): Пароль для доступа к менеджеру (по умолчанию 'paswsord').
    - SECRET_KEY (str): Секретный ключ, генерируемый с использованием secrets.token_hex
    - RUN_BOT (bool): Флаг, проверяющий и указывающий, запущен ли бот в данный момент.
    - BOT_FILE (str): Имя файла с основным кодом бота в папке bot (по умолчанию 'bot.py').
    - COUNT_AUTH (int): Количество попыток аутентификации в менеджер, после создается Error в logg/log.log.
    """
    TOKEN = os.getenv('TOKEN', None)
    ADMIN_ID = os.getenv('ADMIN_ID', None)
    PASSWORD = os.getenv('PASSWORD', 'paswsord')
    SECRET_KEY = secrets.token_hex(16)
    RUN_BOT = is_bot_running()
    BOT_FILE = os.getenv('BOT_FILE', 'bot.py')
    COUNT_AUTH = 3

