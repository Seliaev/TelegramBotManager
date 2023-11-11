# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
import subprocess
from core.config.config import Config as config
from core.logg.logger import set_logger
from core.utils.get_stats import get_bot_process

logger = set_logger('flask')
logger.info('START FLASK APP')


app = Flask(__name__, template_folder='html')
app.config.from_object(config)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin):
    """
    Класс пользователя, используемый Flask-Login.

    Arguments:
        id: Идентификатор пользователя.
    """
    pass

@login_manager.user_loader
def load_user(user_id) -> User:
    """
    Функция загрузки пользователя для Flask-Login.

    Arguments:
        user_id: Идентификатор пользователя.

    Returns:
        User: Объект пользователя.
    """
    user = User()
    user.id = user_id
    return user

@app.route('/login', methods=['GET', 'POST'])
def login() -> redirect or render_template:
    """
    Обработчик маршрута для страницы входа в систему.

    Returns:
        Страница входа или страница ошибки аутентификации.
    """
    if request.method == 'POST':
        password = request.form['password']

        if check_password_hash(generate_password_hash(app.config['PASSWORD']), password):
            user = User()
            user.id = 1
            login_user(user)
            return redirect(url_for('index'))
        elif app.config['COUNT_AUTH'] == 1:
            user_ip = request.remote_addr
            app.config['COUNT_AUTH'] = 3
            logger.warning(f"The user: {user_ip} used {app.config['COUNT_AUTH']} attempts of an incorrect password!")
            return render_template('no_login.html')
        else:
            app.config['COUNT_AUTH'] -= 1
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout() -> redirect:
    """
    Обработчик маршрута для выхода из системы.
0
    Returns:
        Перенаправление на страницу входа.
    """
    logout_user()
    logger.debug(f"Successful logout and redirect to the login")
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index() -> render_template:
    """
    Обработчик маршрута для главной страницы.

    Returns:
        Главная страница.
    """
    logger.debug(f"Successful login and redirect to the index")
    return render_template('index.html')

@app.route('/start_bot')
@login_required
def start_bot() -> redirect:
    """
    Обработчик маршрута для запуска бота.
    Запускает бот, если он не запущен.

    Returns:
        Перенаправление на главную страницу или сообщение об ошибке.
    """
    try:
        if app.config['RUN_BOT'] == False:
            subprocess.Popen(['python', f"core/bot/{app.config['BOT_FILE']}"])
            app.config['RUN_BOT'] = True
            logger.debug(f"Successful START bot {app.config['BOT_FILE']} and redirect to the index")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    except Exception as ex:
        logger.exception(ex)
        return f"Error starting bot: {str(ex)}"

@app.route('/stop_bot')
@login_required
def stop_bot() -> redirect:
    """
    Обработчик маршрута для остановки бота.
    Завершает работу бота

    Returns:
        Перенаправление на главную страницу или сообщение об ошибке.
    """
    try:
        subprocess.run(['pkill', '-f', f"core/bot/{app.config['BOT_FILE']}"])
        app.config['RUN_BOT'] = False
        logger.debug(f"Successful STOP bot {app.config['BOT_FILE']} and redirect to the index")
        return redirect(url_for('index'))
    except Exception as ex:
        logger.exception(ex)
        return f"Error stopping bot: {str(ex)}"

@app.route('/restart_bot')
@login_required
def restart_bot() -> redirect:
    """
    Обработчик маршрута для перезапуска бота.
    Проходит по функциям остановки и запуска бота

    Returns:
        Перенаправление на главную страницу или сообщение об ошибке.
    """
    stop_bot()
    start_bot()
    logger.debug(f"Successful RESTART bot {app.config['BOT_FILE']} and redirect to the index")
    return redirect(url_for('index'))

@app.route('/stats')
@login_required
def stats() -> redirect or render_template:
    """
    Обработчик маршрута для отображения статистики использования ресурсов процессом бота

    Returns:
        Страница со статистикой или перенаправление на главную страницу.
    """
    bot_process = get_bot_process()
    if bot_process:
        cpu_percent = bot_process.cpu_percent(interval=1)
        memory_percent = bot_process.memory_percent()
        logger.debug(f"Successful get stats to - python {app.config['BOT_FILE']}")
        return render_template('stats.html', cpu_percent=cpu_percent, memory_percent=memory_percent)
    else:
        logger.debug(f"The process with the bot {app.config['BOT_FILE']} is not running")
        return redirect(url_for('index'))

