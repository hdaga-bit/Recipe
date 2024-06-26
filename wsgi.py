import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "C:\xampp\htdocs\recipe_database")

from app import app as application
