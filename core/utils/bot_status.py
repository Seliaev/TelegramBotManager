import psutil

def is_bot_running() -> bool:
    """
    Проверяет, запущен ли процесс бота с именем 'bot.py'.

    Returns:
        bool: True, если процесс бота запущен, в противном случае - False.
    """
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['name'] == 'python' and 'bot.py' in process.info['cmdline']:
            return True
    return False
