import os
import dotenv

# Load from dotenv only in development
if 'DOCKER' not in os.environ:
    dotenv.load_dotenv()

ENV = os.environ.get("ENV", "production")

# App host
HOST = os.environ.get("HOST", '0.0.0.0')
PORT = os.environ.get("PORT", 8000)
VERSION = '1.0.0'

# UI
SUPPORTED_UI_IMPLEMENTATIONS = ['vue', 'react']
UI = os.environ.get("UI", None)
assert UI in SUPPORTED_UI_IMPLEMENTATIONS, f"Currently supported UI implementations are {SUPPORTED_UI_IMPLEMENTATIONS}"

# Logger
LOGS_FOLDER = os.path.join(os.getcwd(), "server", "logs")

# Postgres
DB_TYPE = 'postgres'
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_URI = '{db_type}://{user}:{password}@{host}:{port}/{db_name}'.format(
    db_type=DB_TYPE,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    db_name=POSTGRES_DB,
)

# Served Folders
TEMPLATE_FOLDER = os.path.join(os.getcwd(), "server", UI, "build")
STATIC_FOLDER = os.path.join(TEMPLATE_FOLDER, 'static')
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

# Debug mode
DEBUG = ENV == 'development'
