# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys

import pyaws_lambda
from pyaws_lambda import commands

if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)


def main(args=None):
    context = pyaws_lambda.Context.default_context()
    commands.make_dist_package(context)
    commands.deploy_functions(context)


if __name__ == '__main__':
    sys.exit(main(args=sys.argv))
