# -*- coding: utf-8 -*-
"""
bgw_dl
~~~~~~~~~~~~~~~~~~~

Biblegateway.com Bible audio downloader

:copyright: (c) 2015 by vonpupp
:licence: MIT, see LICENCE for more details
"""
from __future__ import absolute_import, unicode_literals
import logging

# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t=Vanguard Boilerplate
__banner__ = r"""
╦  ╦┌─┐┌┐┌┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╗╔╝├─┤││││ ┬│ │├─┤├┬┘ ││  by vonpupp
 ╚╝ ┴ ┴┘└┘└─┘└─┘┴ ┴┴└──┴┘
"""

__title__ = 'bgw-dl'
__summary__ = 'Biblegateway.com Bible audio downloader'
__uri__ = 'https://github.com/vonpupp/bgw-dl'

__version__ = '0.0.1'

__author__ = 'vonpupp'
__email__ = 'vonpupp@gmail.com'

__license__ = 'MIT'
__copyright__ = 'Copyright 2015 vonpupp'

# the user should dictate what happens when a logging event occurs
logging.getLogger(__name__).addHandler(logging.NullHandler())
