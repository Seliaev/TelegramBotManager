# Раздел с ботом

В этом разделе вы можете разместить своего телеграм бота для запуска из веб-менеджера.

Веб-менеджер поставляется с тестовым ботом. Рекомендуется его удалить.
 ```bash
 rm core/bot/bot.py
 ```

## Установка бота

1. Клонируйте репозиторий с вашим ботом:

   ```bash
   git clone https://github.com/ваш_профиль/ваш_репозиторий.git
   cd ваш_репозиторий
     ```
2. Установите зависимости бота, если они у вас есть.
    ```bash
     pip install -r requirements.txt
    ```
3. Структура бота должна быть:
    ```plaintext
    |-- core/
    |   |-- __init__.py
    |   |-- bot/
    |       |-- __init__.py
    |       |-- ваш_исполняемый_файл.py
    |       |-- ваши файлы и папки для бота
    |   |-- config/
    |       |-- .env
    |       |-- __init__.py
    |       |-- config.py
    |   |-- flask/
    |       |-- html/
    |           |-- index.html
    |           |-- login.html
    |           |-- no_login.html
    |           |-- no_process.html
    |           |-- stats.html
    |       |-- static/
    |           |-- styles.css
    |       |-- __init__.py
    |       |-- app.py
    |   |-- logg/
    |       |-- __init__.py
    |       |-- log.log
    |       |-- logger.py
    |   |-- utils/
    |       |-- __init__.py
    |       |-- bot_status.log
    |       |-- get_stats.py
    |-- README.md
    |-- requirements.txt
    |-- main.py
   ```
   
```plaintext
Примечание: Замените "ваш_профиль" и "ваш_репозиторий" на реальные значения вашего профиля и репозитория GitHub.
```