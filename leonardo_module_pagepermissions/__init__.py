
from django.apps import AppConfig

try:
    from local_settings import APPS
except ImportError:
    pass

default_app_config = 'leonardo_module_pagepermissions.PagePermissonsConfig'


class Default(object):
    if 'leonardo_module_pagepermissions' in APPS:
        apps = [
            'pagepermissions',
            'leonardo_module_pagepermissions',
        ]

        page_extensions = [
            'pagepermissions.extension',
        ]


class PagePermissonsConfig(AppConfig, Default):
    name = 'leonardo_module_pagepermissions'
    verbose_name = ("Page Permissions")


default = Default()
