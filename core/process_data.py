# -*- coding: utf-8 -*-
"""
Author: harrisonhxy
Program: process_data
Introduction: 
"""

from core.utils import *


def filter_data(df):
    df = df.loc[:, ["股票代码", "证券简称", "首发主承销商"]]
    df["首发主承销商"] = df["首发主承销商"].str.split(",").str[0].str.strip()
    return df


def classify_broker(broker_name, broker_dic):
    if pd.isna(broker_name):
        return "对照组", 0

    for key, keywords in broker_dic.items():
        sort_keywords = sorted(keywords, key=len, reverse=True)
        for keyword in sort_keywords:
            if keyword in broker_name:
                return key, 1
    return "对照组", 0
