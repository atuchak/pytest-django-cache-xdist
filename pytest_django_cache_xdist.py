from copy import copy

import pytest
from pytest_django.lazy_django import skip_if_no_django


@pytest.fixture(autouse=True, scope='session')
def django_cache_add_xdist_key_prefix(request):
    skip_if_no_django()

    xdist_prefix = getattr(request.config, 'slaveinput', {}).get('slaveid')

    if not xdist_prefix:
        return

    from django.conf import settings
    from django.core.cache import caches, _create_cache

    for cache_alias, cache_settings in settings.CACHES.items():
        new_prefix = xdist_prefix + '_' + cache_settings.get('KEY_PREFIX', '')
        cache_settings['KEY_PREFIX'] = new_prefix
        new_cache = copy(settings.CACHES[cache_alias])
        new_cache['KEY_PREFIX'] = new_prefix
        settings.CACHES[cache_alias] = new_cache

        if getattr(caches._caches, 'caches', None) is None:
            continue

        caches._caches.caches[cache_alias] = _create_cache(cache_alias)
