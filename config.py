import json

config_file = 'web/config.json'

def load_config():
    with open(config_file, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

config = load_config()

BOT_TOKEN = config['BOT_TOKEN']
ITEMS_URL = config['ITEMS_URL']
DEVELOPER_ID = config['DEVELOPER_ID']
SECRET = config['SECRET']
CHECK_INTERVAL = config['CHECK_INTERVAL']
