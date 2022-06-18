# Copyright (c) 2022 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

from packaging.version import Version

from smart_prom_next import __version__


def test__version__():
    # if __version__ does not conform to PEP 440 InvalidVersion will be raised
    Version(__version__)
