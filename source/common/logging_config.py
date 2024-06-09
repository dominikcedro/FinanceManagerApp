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
            'level': 'ERROR',
        },
        'analysis': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'operations': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'database': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'visualization': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        '__main__': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'ERROR',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(module)s %(name)s: %(message)s',
        },
    },
}