from __future__ import unicode_literals

from django.apps import AppConfig


class UseraccountsConfig(AppConfig):
    name = 'useraccounts'

    def ready(self):
        from . import signals
