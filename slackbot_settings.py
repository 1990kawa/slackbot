# -*- coding: utf-8 -*-

API_TOKEN = os.environs.get('API_TOKEN', None)

DEFAULT_REPLY = "ほげほげ"

PLUGINS = [
    'slackbot.plugins',
    'mybot.plugins'
]

ERRORS_TO = "general"
ERRORS_TO = "kawashima"


