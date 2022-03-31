
"""Flask configuration variables."""
from os import environ
from dotenv import load_dotenv
import utils
# Load environment variables from file .env, stored in this directory.
load_dotenv()


class Config:
    """Set Flask configuration from .env file."""

    # Flask configuration
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')
    TESTING = environ.get('TESTING')

    # Database configuration
    DATABASE = utils.getPath(environ.get("DATABASE_PATH"))
