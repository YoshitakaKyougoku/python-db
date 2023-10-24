from dotenv import load_dotenv
load_dotenv()

import os

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DATABASE = os.getenv('DATABASE')