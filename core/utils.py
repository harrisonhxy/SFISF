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


def filter_data(df):
    df = df.loc[:, ["股票代码", "证券简称", "首发主承销商"]]
    df["首发主承销商"] = df["首发主承销商"].str.split(",").str[0].str.strip()
    return df


def classify_broker(broker_name, broker_dic):
    '''
    根据券商名称对照表broker_dic，将df["首发主承销商"]中的券商分为对照组或处理组，并返回df[["归属券商", "treat"]]。

    df["首发主承销商"]中的券商不在broker_dic中的，归属券商为"对照组"，treat为0；
    在broker_dic中的，归属券商为对应的key，treat为1。

    :param broker_name: df["首发主承销商"]的值
    :param broker_dic: 券商名称对照表，格式为{"券商名称": ["别名1", "别名2", ...]}
    :return:
    '''
    if pd.isna(broker_name):
        return "对照组", 0

    for key, keywords in broker_dic.items():
        sort_keywords = sorted(keywords, key=len, reverse=True)
        for keyword in sort_keywords:
            if keyword in broker_name:
                return key, 1
    return "对照组", 0


def merge_data(df1, df2, on=None, how="outer"):
    return pd.merge(df1, df2, on=on, how=how)
