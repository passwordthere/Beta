import investpy
import pandas as pd
from datetime import datetime


def get_index():
    # 列出中国所有可用的指数
    indices = investpy.indices.get_indices(country='china')
    indices.reset_index(inplace=True)
    indices.to_csv('get_index.csv', index=False)
    # print(indices.head(100))


def get_csv():
    end_date = datetime.now().strftime('%d/%m/%Y')
    data = investpy.indices.get_index_historical_data(index='Shanghai',
                                                    country='china',
                                                    from_date='01/01/2023',
                                                    to_date=end_date)

    data.reset_index(inplace=True)
    print(data.head())
    data.to_csv('shanghai_composite_index.csv', index=False)

# get_index()
get_csv()