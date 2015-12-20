#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bgw_dl.__main__
~~~~~~~~~~~~~~~~~~~~~

The main entry point for the command line interface.

Invoke as ``bgw_dl`` (if installed)
or ``python -m bgw-dl`` (no install required).
"""
from __future__ import absolute_import, unicode_literals
import logging
import sys

from bgw_dl.log import configure_stream

logger = logging.getLogger(__name__)


def cli():
    """Add some useful functionality here or import from a submodule."""
    # configure root logger to print to STDERR
    configure_stream(level='DEBUG')

    # launch the command line interface
    logger.debug('Booting up command line interface')

    # ...oops, it wasn't implemented yet!
    logger.error('Please implement the command line interface!')
    raise NotImplementedError('Vanguard Boilerplate CLI not implemented yet')


if __name__ == '__main__':
    # exit using whatever exit code the CLI returned
    sys.exit(cli())
