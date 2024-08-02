# GTKY Item Panel

## Introduction
This project provides a web-based admin panel to manage a Discord bot, view logs, and update configurations. The admin panel includes features to start and stop the bot, check its status, view logs, and update the bot's configuration.
This all on discord /commands

## passworld defult
passworld defult is admin
Passworld change at: web/config.json

### Prerequisites
- Python 3.8 or later
- XAMPP (for Apache server)
- Git

### Python Setup

1. Create and activate a virtual environment (optional but recommended).
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. Install Python dependencies.
pip install -r requirements.txt

3. Open you XAMPP!
Open config of Apache (httpd.conf)
then change the url of the web/index.php and etc!
DocumentRoot "C:/xampp/htdocs"
<Directory "C:/xampp/htdocs">


3. Run the Flask server.
python web/app.py

### Clone the Repository
Clone the repository to your local machine.
```sh
git clone https://github.com/Spartakingdom/GTPS-item-bot-main
cd gtky-item-panel
pip install -r requirements.txt