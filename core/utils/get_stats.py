from typing import Optional

import psutil

def get_bot_process() -> Optional[psutil.Process]:
    """
    Получает информацию о процессе бота с именем 'bot.py'.

    Returns:
        Optional[psutil.Process]: Объект psutil.Process, представляющий запущенный процесс бота, или None, если процесс не найден.
    """
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['cmdline'] is not None:
            if process.info['name'] == 'python' and 'core/bot/bot.py' in process.info['cmdline']:
                return process
    return None