import pandas as pd

def standardize_vn_index_data(data_path: str = "C:/stock/"):
       '''
       Standardize vnindex data from cophieu68 with format of vndirect api
       '''           
       df_source = pd.read_csv(data_path + "data/cophieu68/excel_^vnindex.csv")
       df_source.columns

       df_source.columns = ['symbol', 'tradingDate', 'c1', 'c2', 'c3',
              'c4', 'volume', 'open', 'high', 'low', 'close',    
              'c5', 'c6', 'c7']

       df_target = pd.read_csv(data_path + "data/stock_price/stock_price_2021.csv")
       df_target.columns


       df_dummy = pd.DataFrame([], columns=df_target.columns)

       df_vnindex = pd.concat([df_dummy, df_source], axis=0, ignore_index=True)

       df_vnindex = df_vnindex[['id', 'symbol', 'open', 'close', 'high', 'low', 'average',
              'volume', 'value', 'ptVolume', 'ptValue', 'change', 'percentage',
              'object', 'tradingDate']]


       df_vnindex['tradingDate'] = df_vnindex['tradingDate'].apply(lambda s : str(s)[0:4] + '-' + str(s)[4:6] + '-' + str(s)[6:8])

       df_vnindex.to_csv(data_path + "data/stock_price/0-vnindex.csv")
       return True

