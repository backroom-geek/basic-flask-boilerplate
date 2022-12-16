from logging import root
import util.constants as const


class Config(object):
    """Base config, uses staging database server."""
    PORT = 8000
    APP_NAME = "MY BOILERPLATE APP"
    DEBUG = True


class ProductionConfig(Config):
    """Uses production database server."""
    PORT = 8080


class DevelopmentConfig(Config):
    PORT = 8000
