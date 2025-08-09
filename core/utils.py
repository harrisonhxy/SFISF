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


def load_data(file_path, file_type="excel"):
    if file_type == "excel":
        return pd.read_excel(file_path)
    elif file_type == "csv":
        return pd.read_csv(file_path, encoding="utf-8-sig")
    else:
        raise ValueError(f"Unsupported file type: {file_type}. Supported types are: excel, csv.")


def merge_data(df1, df2, on=None, how="outer"):
    return pd.merge(df1, df2, on=on, how=how)
