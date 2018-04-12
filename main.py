"""Lambda function that executes pydocstyle, a static file linter."""
import logging
import sys

from lintipy import Handler

root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(logging.StreamHandler(sys.stdout))


def handle(*args, **kwargs):
    Handler('PEP257', 'pydocstyle', '.')(*args, **kwargs)
