"""Lambda function that executes pydocstyle, a static file linter."""
import logging
import sys

from lintipy import CheckRun

root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(logging.StreamHandler(sys.stdout))


def handle(*args, **kwargs):
    CheckRun('PEP257', 'pydocstyle', '.')(*args, **kwargs)
