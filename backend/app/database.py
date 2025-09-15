from sqlalchemy import create_engine
from os import environ
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(environ['DATABASE_URL'])