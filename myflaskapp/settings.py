# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import os
from environs import Env

env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'

# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:deyiUther943@localhost:3306/quatek"
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(env.str('SQL_USER'), env.str('SQL_PASSWORD'),
#                                                                   env.str('SQL_HOST'), env.str('SQL_PORT'),
#                                                                   env.str('SQL_DB_NAME'))
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(os.getcwd(), 'data.sqlite')

SECRET_KEY = 'not-so-secret'
BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
