import os

SECRET_KEY = 'key'

REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_DB = 1

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'KEY_FUNCTION': 'test_project.helpers.make_key',
        'LOCATION': [
            'redis://{host}:{port}/'.format(host=REDIS_HOST, port=REDIS_PORT),
        ],
        'OPTIONS': {
            'DB': REDIS_DB,
            'PASSWORD': 'yadayada',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 5,
                'timeout': 5,
            },
            'MAX_CONNECTIONS': 5,
            'PICKLE_VERSION': -1,
        },
    },
}
