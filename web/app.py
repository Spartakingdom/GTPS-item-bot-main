from flask import Flask, request
import subprocess
import os
import signal
import psutil
import datetime
import json

app = Flask(__name__)
bot_process = None

config_file = 'web/config.json'

def load_config():
    with open(config_file, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

config = load_config()
SECRET = config['SECRET']
LOG_FILE = 'web/logs.txt'

def log_action(action, status):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {action} - {status}\n")

@app.route('/')
def index():
    return "Admin Panel"

@app.route('/start_bot')
def start_bot():
    secret = request.args.get('secret')
    if secret != SECRET:
        log_action('start_bot', 'Unauthorized')
        return "Unauthorized", 403
    
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(["python", "bot.py"])
        log_action('start_bot', 'Bot started')
        return "Bot started"
    else:
        log_action('start_bot', 'Bot is already running')
        return "Bot is already running"

@app.route('/stop_bot')
def stop_bot():
    secret = request.args.get('secret')
    if secret != SECRET:
        log_action('stop_bot', 'Unauthorized')
        return "Unauthorized", 403
    
    global bot_process
    if bot_process is not None:
        process = psutil.Process(bot_process.pid)
        for child in process.children(recursive=True):
            child.kill()
        process.kill()
        bot_process = None
        log_action('stop_bot', 'Bot stopped')
        return "Bot stopped"
    else:
        log_action('stop_bot', 'Bot is not running')
        return "Bot is not running"

@app.route('/status')
def status():
    secret = request.args.get('secret')
    if secret != SECRET:
        log_action('status', 'Unauthorized')
        return "Unauthorized", 403
    
    global bot_process
    if bot_process is None:
        log_action('status', 'Bot is not running')
        return "Bot is not running"
    else:
        log_action('status', 'Bot is running')
        return "Bot is running"

@app.route('/update_config', methods=['POST'])
def update_config():
    secret = request.form.get('secret')
    if secret != SECRET:
        log_action('update_config', 'Unauthorized')
        return "Unauthorized", 403

    new_config = {
        "BOT_TOKEN": request.form.get('bot_token'),
        "ITEMS_URL": request.form.get('items_url'),
        "DEVELOPER_ID": request.form.get('developer_id'),
        "SECRET": config['SECRET'],  # Keep the existing secret
        "CHECK_INTERVAL": config['CHECK_INTERVAL']  # Keep the existing interval
    }
    save_config(new_config)
    log_action('update_config', 'Configuration updated')
    return "Configuration updated"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
