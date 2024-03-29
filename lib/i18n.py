from __future__ import unicode_literals

from pyramid.events import (
    BeforeRender,
    NewRequest,
    subscriber,
)

from pyramid.i18n import (
    TranslationStringFactory,
    get_localizer
)

_ = TranslationStringFactory('test_work')

default_domain = 'test_work'


@subscriber(BeforeRender)
def add_renderer_globals(event):
    request = event['request']
    event['_'] = request.translate
    event['localizer'] = request.localizer


@subscriber(NewRequest)
def add_localizer(event):
    # if event.request.accept_language:
    #     accepted = event.request.accept_language
    #     if accepted.header_value == 'id':
    #         event.request._LOCALE_ = 'id'
    #     else:
    #         event.request._LOCALE_ = 'zh_Hant'

    request = event.request
    localizer = get_localizer(request)

    def auto_translate(*args, **kwargs):
        return localizer.translate(_(*args, **kwargs))

    request.localizer = localizer
    request.translate = auto_translate


def normalize_locale_name(locale_name):
    """Normalize locale name, for example, zh_tw will be normalized as zh_TW."""
    import locale
    normalized = locale.normalize(locale_name)
    if normalized == locale_name:
        return normalized
    parts = normalized.split('.')
    result = parts[0]
    return result


class LocalizerFactory(object):
    """Localize string."""

    def __init__(self, domain=default_domain):
        self.domain = domain

    def __call__(self, request):
        return self.get_localizer(request)

    def get_localizer(self, request):
        from pyramid.i18n import get_localizer
        localizer = get_localizer(request)
        return Localizer(localizer, self.domain)


class Localizer(object):
    """A proxy for localizer, bound with domain argument."""

    def __init__(self, localizer, domain):
        self.localizer = localizer
        self.domain = domain

    def __call__(self, *args, **kwargs):
        return self.translate(*args, **kwargs)

    def translate(self, tstring, mapping=None):
        result = self.localizer.translate(tstring,
                                          domain=self.domain,
                                          mapping=mapping)
        return result

    def pluralize(self, singular, plural, n, mapping=None):
        result = self.localizer.pluralize(singular, plural, n,
                                          domain=self.domain,
                                          mapping=mapping)
        return result
