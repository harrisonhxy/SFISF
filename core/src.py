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
IPO_DATA = os.path.join(settings.DATA_DIR, "IPO承销商全部A股.xlsx")
STOCK_YIELD_DATA = os.path.join(settings.DATA_DIR, "股票收益率.xlsx")


def process_ipo_data():
    # 导入IPO承销商数据
    ipo_data = load_data(IPO_DATA)
    ipo_data = filter_data(ipo_data)

    broker_dic = load_json(BROKER_DIC)
    ipo_data[["归属券商", "treat"]] = ipo_data["首发主承销商"].apply(
        lambda x: pd.Series(classify_broker(x, broker_dic))
    )
    ipo_data = ipo_data.rename(columns={"股票代码": "Stkcd"})
    return ipo_data


def process_stock_yield_data():
    # 导入股票收益率数据，Trddt为交易日期，td为时间戳
    stock_yield_data = load_data(STOCK_YIELD_DATA)
    return stock_yield_data


def main():
    ipo_data = process_ipo_data()
    stock_yield_data = process_stock_yield_data()

    # 合并数据
    merged_data = merge_data(ipo_data, stock_yield_data, on="Stkcd", how="outer")

    # 导出数据
    os.makedirs(settings.OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(settings.OUTPUT_DIR, "treatment.csv")
    merged_data.to_csv(output_file, index=False, encoding="utf-8-sig")

    return merged_data
