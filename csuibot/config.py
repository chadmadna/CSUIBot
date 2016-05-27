from os import environ


APP_ENV = environ.get('APP_ENV', 'development')
DEBUG = environ.get('DEBUG') == 'true'
MICROSOFT_SEARCH_TOKEN = environ.get('MICROSOFT_SEARCH_TOKEN')
TELEGRAM_BOT_TOKEN = environ.get('TELEGRAM_BOT_TOKEN', 'somerandomstring')
LOG_LEVEL = environ.get('LOG_LEVEL', 'WARNING')
WEBHOOK_HOST = environ.get('WEBHOOK_HOST', '127.0.0.1')
MUSIXMATCH_API = environ.get('MUSIXMATCH_API')
COMPUTER_VISION_KEY = environ.get('COMPUTER_VISION_KEY', 'morerandomstring')
CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
