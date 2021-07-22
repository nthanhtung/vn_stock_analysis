from numpy import append
import xxx.load.to_df as td
import pandas as pd
import pandas_ta as ta
import datetime as dt

class xxx_tram_anh():
    def __init__(self) -> None:
        self.custom_strategy = ta.Strategy(
            name="Momo and Volatility",
            description="SMA 20,50, BBANDS, RSI, MACD and Volume SMA 20",
            ta=[
                {"kind": "sma", "length": 20, "append":"True"},
                {"kind": "sma", "length": 50, "append":"True"},
                {"kind": "bbands", "length": 20, "append":"True"},
                {"kind": "rsi"},
                {"kind": "macd", "fast": 8, "slow": 21},
                {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME", "append":"True"},
            ]
        )
        self.candle_pattern = ["doji", "shootingstar", "hammer", "hangingman", "eveningstar", "morningstar", "invertedhammer"]

    def calculate_ta(self, df_source, symbol_current):
        try:
            print(f"----------start calculate ta for {symbol_current}---------")
            df_current = df_source[df_source["symbol"] == symbol_current]
            df_col_list = ["open", "high", "low", "close", "volume", "adj_close"]
            df_current = df_current[df_col_list]
            # To run your "Custom Strategy"
            df_current.ta.strategy(self.custom_strategy)
            df_current.ta.cdl_pattern(name = self.candle_pattern, append = True)
            df_current["VOLUME_VS_MA20"] = df_current["volume"]/df_current["VOLUME_SMA_20"]
            df_current["symbol"] = symbol_current
            # Add signal column
            df_current["X2 VOLUME SMA20"] = df_current["VOLUME_VS_MA20"] > 2
            df_current["X1.5_VOLUME SMA20"] = df_current["VOLUME_VS_MA20"] > 1.5
            df_current["X0.5_VOLUME SMA20"] = df_current["VOLUME_VS_MA20"] < -0.5
            df_current["MA20 > MA50"] = df_current["SMA_20"] > df_current["SMA_50"]
            df_current["PRICE > BBU20"] = df_current["close"] > df_current["BBU_20_2.0"]
            df_current["PRICE < BBL20"] = df_current["close"] < df_current["BBL_20_2.0"]
            df_current["RSI > 70"] = df_current["RSI_14"] > 70
            df_current["RSI < 30"] = df_current["RSI_14"] < 30
            df_current["MA20 X MA50"] = ta.cross(df_current.ta.sma(20), df_current.ta.sma(50), above=True)
            df_current["MACD X 0"] = df_current["MACD_8_21_9"].between(-0.2,0.2)
            print("------------done---------")
        except Exception as e:
            print(e)
        return df_current

    def transform_df(self, df_before):
        df_before["adj_close"] = df_before["close"]
        df_before.set_index(pd.DatetimeIndex(df_before["tradingDate"]), inplace=True)
        df_after = df_before.sort_index(ascending=True)        
        return df_after

    def to_csv(self, symbol_list, data_path: str = "C:/stock/", history: bool = False):
        # type of calculation : history or current year
        year_current = dt.datetime.now().year
        if history:
            df = td.csv_path_to_df(path = data_path + 'data/stock_price', file_name_to_exclude = f'stock_price_{year_current}.csv')
            export_file_name = "history"
        else:
            df = pd.read_csv(data_path + 'data/stock_price' + f'/stock_price_{year_current}.csv')
            export_file_name = "new"
        # add new column to match the ta library
        df = self.transform_df(df)
        appended_data = list(map(lambda x: self.calculate_ta(df_source=df, symbol_current=x), symbol_list))
        appended_data = pd.concat(appended_data)
        appended_data.to_csv(data_path + f"data/stock_ta/{export_file_name}.csv")
        return True
    
    def append_csv_vnindex(self, data_path: str = "C:/stock/"):
        df = pd.read_csv(data_path + 'data/stock_price' + f'/0-vnindex.csv')
        df = self.transform_df(df)
        vn_index_ta = self.calculate_ta(df_source = df, symbol_current= "^VNINDEX")
        vn_index_ta.to_csv(data_path + "data/stock_ta/new.csv", mode="a", header=False)
        return True        
    

################
# data_path = "C:/Users/tung.nguyen/Desktop/0 Project/stock/"
# year_current = 2021
# x = xxx_tram_anh()
# df = pd.read_csv(data_path + 'data/stock_price' + f'/0-vnindex.csv')
# df = x.transform_df(df_before=df)
# df = x.calculate_ta(df, "^VNINDEX")