#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8

import sys
import os
from controller.Application import Application


if __name__ == "__main__":
    app = Application(sys.argv, os.path.dirname(__file__))
