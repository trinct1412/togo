from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModelsConfig(AppConfig):
    label = 'Models'
    name = 'apps.models'
    verbose_name = _('Models')