from pathlib import Path
import environ

env = environ.Env(DEBUG=(bool, False))

BASE_DIR = environ.Path(__file__) - 2
