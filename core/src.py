# -*- coding: utf-8 -*-
"""
Author: harrisonhxy
Program: src
Introduction: 
"""
import os

from conf import settings
from core.process_data import *

BROKER_DIC = os.path.join(settings.DATA_DIR, "brokers.json")
STOCK_DATA = os.path.join(settings.DATA_DIR, "IPO承销商全部A股.xlsx")


def main():
    data = load_data(STOCK_DATA)
    data = filter_data(data)

    broker_dic = load_json(BROKER_DIC)
    data[["归属券商", "treat"]] = data["首发主承销商"].apply(
        lambda x: pd.Series(classify_broker(x, broker_dic))
    )

    os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(settings.OUTPUT_DIR, "treatment.csv")
    data.to_csv(output_file, index=False, encoding="utf-8-sig")

    return data
