# -*- coding: utf-8 -*-
"""
Author: harrisonhxy
Program: utils
Introduction: 
"""
import json

import pandas as pd


def load_json(broker_dic_path):
    with open(broker_dic_path, "r", encoding="utf-8") as f:
        broker_dic = json.load(f)
    return broker_dic

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df
