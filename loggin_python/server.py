import logging

from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

# create a console logger
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
app.logger.addHandler(ch)

@app.route('/')
def index():
    app.logger.info('This is a Python/Flask sample API')
    return "This is a Python/Flask sample API"
@app.route('/info')
def info():
    app.logger.info('This is an info message')
    return "info"
@app.route('/warning')
def warning():
    app.logger.warning('This is a warning message')
    return "warning"
@app.route('/error')
def error():
    app.logger.error('This is an error message')
    return "error"
@app.route('/critical')
def critical():
    app.logger.critical('This is a critical message')
    return "critical"

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0")
