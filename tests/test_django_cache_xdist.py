import pickle
import random
import string

import redis
from django.conf import settings
from django.core.cache import cache

from tests.test_project.helpers import make_key


def generate_rnd_str(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def test_that_django_cache_key_is_prefixed_by_fixture(request):
    django_key = generate_rnd_str()
    django_value = generate_rnd_str()
    TIMEOUT = 5
    cache.set(django_key, django_value, TIMEOUT)

    redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

    xdist_prefix = getattr(request.config, 'slaveinput', {}).get('slaveid')
    assert xdist_prefix is not None, 'Run pytest with xdist'

    redis_key = make_key(django_key, xdist_prefix + '_', 0)
    assert redis_key in redis_client.keys(pattern='{xdist_prefix}*'.format(xdist_prefix=xdist_prefix))
    assert pickle.loads(redis_client.get(redis_key)) == django_value
