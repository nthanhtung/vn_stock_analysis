import requests as re
import pandas as pd
import xxx.utility as u
import datetime as dt

class single_request():
    '''
    You can inherit this class to develop nested api call
    '''      
    def __init__(self, data_path: str = "C:/stock/", stock_symbol_list: list = ["HPG", "VNM"]) -> None:
        self.data_path = data_path
        self.stock_symbol_list = stock_symbol_list

    def get_stock_price(self, symbols : list = ["VNM", "HPG"], fromDate : str = "2010-01-01", toDate : str = "2010-12-31") -> list:
        '''
        Get stock price using vndirect api with 1 request
        '''           
        stock_price = []
        job_log = []
        for symbol in symbols:
            try:
                assert symbol in self.stock_symbol_list, "stock symbols not found"
                stock_price_1_symbol =  re.get(url= "https://finfoapi-hn.vndirect.com.vn/stocks/adPrice", params = {"symbols":symbol ,"fromDate":fromDate, "toDate": toDate} )
                stock_price = stock_price + stock_price_1_symbol.json()['data']
                assert stock_price != [], "stock data not found"
                job_log = job_log + [{ "symbols" : symbol, "fromDate" : fromDate, "toDate" : toDate , "status":"Success", "ts": str(dt.datetime.utcnow()) }]
            except Exception as e:
                job_log = job_log + [{ "symbols" : symbol, "fromDate" : fromDate, "toDate" : toDate , "status":e, "ts": str(dt.datetime.utcnow()) }]
        return stock_price, job_log #list

    def get_finance_data(self, symbols : list = ["VNM", "HPG"], fromDate : str = "2010-01-01", toDate : str = "2010-12-31", type : str = "quarter") -> None:
        '''
        Get finance info using vndirect api with 1 request
        '''          
        finance_data = []
        job_log = []

        for symbol in symbols:
            try:
                assert symbol in self.stock_symbol_list, "stock symbols not found"
                if type == "quarter":
                    param_final = {"secCodes":symbol ,"fromDate":fromDate, "toDate": toDate, "reportTypes":"QUARTER"}
                else:
                    param_final = {"secCodes":symbol ,"fromDate":fromDate, "toDate": toDate}
                finance_data_1_symbol =  re.get(url= "https://finfo-api.vndirect.com.vn/v3/stocks/financialStatement", params = param_final )
                finance_data_1_symbol_list = list(map(lambda x: x['_source'] , finance_data_1_symbol.json()['data']['hits']))
                finance_data = finance_data + finance_data_1_symbol_list
                assert finance_data != [], "stock data not found"
                job_log = job_log + [{ "symbols" : symbol, "fromDate" : fromDate, "toDate" : toDate , "status":"Success", "ts": str(dt.datetime.utcnow()) }]
            except Exception as e:
                job_log = job_log + [{ "symbols" : symbol, "fromDate" : fromDate, "toDate" : toDate , "status":e, "ts": str(dt.datetime.utcnow()) }]
        return finance_data, job_log #list

    def get_stock_list(self):
        '''
        Get stock meta data (dimension data) using vndirect api with 1 request
        '''          
        url = "https://finfoapi-hn.vndirect.com.vn/stocks/"
        df = pd.DataFrame(re.get(url).json()['data'])
        df.to_csv(self.data_path + 'data/dim/stock.csv')
        return True


class mass_request(single_request):
    '''
    inherit class single_request
    '''
    def __init__(self, data_path: str, stock_symbol_list: list) -> None:
        super().__init__(data_path=data_path, stock_symbol_list=stock_symbol_list)
    def get_stock_price_year_range(self, symbols: list = ["VNM", "HPG"], start_y: int = 2021, end_y: int = 2021) -> True:    
        '''
        use function get_stock_price multiple time to send multiple request
        '''
        print("get_stock_price_year_range")
        date_range = u.generate_year_range(start_y, end_y)
        for i in range(len(date_range)):
            stock_price_full = []
            job_log_full = []
            stock_price, job_log = super().get_stock_price(symbols = symbols, fromDate = date_range[i][0], toDate = date_range[i][1])
            # write job log
            job_log_full = job_log_full + job_log
            job_log_full = pd.DataFrame(job_log_full)
            job_log_full.to_csv(self.data_path + "data/job_log_get_stock_data.csv", mode='a', header=False)
            # write stock price
            if len(stock_price) > 0:
                stock_price_full = stock_price_full + stock_price
                stock_price_df = pd.DataFrame(stock_price_full)
                stock_price_df.to_csv(self.data_path + "data/stock_price/stock_price_{}.csv".format(date_range[i][0][0:4]), mode='w')
            # print message
            print("done {}".format(date_range[i][0]))
        return True

    def get_finance_data_year_range(self, symbols: list = ["VNM", "HPG"], start_y: int = 2021, end_y: int = 2021, type: str = "quarter") -> True:    
        '''
        use function get_finance_data multiple time to send multiple request
        '''           
        print(f"get_finance_data_year_range type = {type}")
        date_range = u.generate_year_range(start_y, end_y)
        for i in range(len(date_range)):
            finance_data_full = []
            job_log_full = []
            finance_data, job_log = super().get_finance_data(symbols = symbols, fromDate = date_range[i][0], toDate = date_range[i][1], type=type)
            # write job log
            job_log_full = job_log_full + job_log
            job_log_full = pd.DataFrame(job_log_full)
            job_log_full.to_csv(self.data_path + "data/job_log_get_finance_data.csv", mode='a', header=False)
            # write stock price
            if len(finance_data) > 0:
                finance_data_full = finance_data_full + finance_data
                finance_data_df = pd.DataFrame(finance_data_full)
                finance_data_df.to_csv(self.data_path + "data/finance_data_{v1}/finance_data_{v1}_{v2}.csv".format(v1 = type, v2 = date_range[i][0][0:4]), mode='w', sep = "|")
            # print message
            print("done {}".format(date_range[i][0]))
        return True


def get_stock_symbol_hose(data_path):
    df = pd.read_csv(data_path + 'data/dim/stock.csv')
    df = df[df["floor"] == "HOSE"]
    stock_list_hose = df["symbol"].to_list()
    return stock_list_hose
