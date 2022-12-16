# -*- coding: utf-8 -*-
import os

import config.config as config
import util.constants as const


def load_config(app):

    print("Loading configuration...")
    _env = os.environ.get(const.ENV, const.DEVELOPMENT)
    if _env == const.PRODUCTION:
        app.config.from_object(config.ProductionConfig())
    elif _env == const.DEVELOPMENT:
        app.config.from_object(config.DevelopmentConfig())
    else:
        app.config.from_object(config.DevelopmentConfig())
