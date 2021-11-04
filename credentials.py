from dotenv import load_dotenv
import os

load_dotenv('.env')

DATABASE_CREDENTIALS = {
    'host': os.getenv('MYSQL_HOST'),
    'port': os.getenv('MYSQL_PORT'),
    'database': os.getenv('MYSQL_DATABASE'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD')
}