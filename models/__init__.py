#!/usr/bin/python3

"""create a unique FileStorage instance for the application."""

from models.engine.file_storage import FileStorage
from models.user import User

storage = FileStorage()
storage.reload()
