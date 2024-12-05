from .base import *
from blog.env import env


DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
