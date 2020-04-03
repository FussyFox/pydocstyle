"""Lambda function that executes pydocstyle, a static file linter."""

from lintipy import CheckRun


handle = CheckRun.as_handler('pydocstyle', 'pydocstyle', '.')
