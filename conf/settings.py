# -*- coding: utf-8 -*-
"""
Author: harrisonhxy
Program: settings
Introduction: 
"""
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent

DATA_DIR = os.path.join(BASE_DIR, "data")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
