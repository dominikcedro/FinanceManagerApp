"""
original author: Dominik Cedro
created: 2024-05-10
license: GSB 3.0
description: This module contains dictionary for logging configuration
"""

LOGGING_CONFIG = {
    'version': 1,
    'loggers': {
        'test': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'analysis': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'operations': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'database': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'visualization': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        '__main__': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(module)s %(name)s: %(message)s',
        },
    },
}