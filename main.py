from core.flask.app import app

if __name__ == '__main__':
    """
    Для запуска в сеть: host='0.0.0.0'
    Для включения режима отладки debug=True
    """
    app.run(port=5000)