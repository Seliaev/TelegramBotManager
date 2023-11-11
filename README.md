# Веб-менеджер для управления скриптом телеграм бота

Веб-менеджер, с доступом по паролю.
Позволяет запускать, останавливать, перезапускать основной скрипт с вашим ботом.

## Требования

Для запуска проекта убедитесь, что у вас установлены следующие зависимости:

>- Flask==3.0.0
>- aiogram==3.1.1
>- Flask-Login==0.6.3
>- psutil==5.9.6
>- python-dotenv==1.0.0
>- Werkzeug==3.0.1

## Установка и Использование

1. Клонируйте репозиторий на свой компьютер.
2. Создайте виртуальное окружение.
3. Установите зависимости с помощью `pip install -r requirements.txt`.
4. Скопируйте, отредактируйте и переименуйте файл tmp.env в .env

### env
>TOKEN=your_bot_token  # Токен вашего бота телеграмм  
>ADMIN_ID=your_admin_id  # Айди телеграмм администратора  
>PASSWORD=your_password  # Пароль для доступа к веб-менеджеру  
>BOT_FILE=bot.py # Имя основного исполняемого файла бота  
   
5. Запустите веб-менеджер с помощью `python main.py`.
6. Перейдите по ссылке: http://127.0.0.1:5000 либо по той, что вам предложит flask



# Web Manager for Controlling Telegram Bot Script

Web manager with password access.
Allows you to start, stop, and restart the main script with your bot.

## Requirements

To run the project, make sure you have the following dependencies installed:

>- Flask==3.0.0
>- aiogram==3.1.1
>- Flask-Login==0.6.3
>- psutil==5.9.6
>- python-dotenv==1.0.0
>- Werkzeug==3.0.1

## Installation and Usage

1. Clone the repository to your computer.
2. Create a virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Copy, edit, and rename the `tmp.env` file to `.env`.

### .env
>TOKEN=your_bot_token  # Your Telegram bot token  
>ADMIN_ID=your_admin_id  # Telegram administrator's ID  
>PASSWORD=your_password  # Password for accessing the web manager  
>BOT_FILE=bot.py  # Name of the main executable file for the bot  

5. Run the web manager with `python main.py`.
6. Navigate to the link: http://127.0.0.1:5000  or the one provided by Flask.
