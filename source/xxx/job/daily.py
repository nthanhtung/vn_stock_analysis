import xxx.extract.api_vn_direct as vd
import xxx.transform.beta_x as bt
import xxx.transform.vnindex as vni
import xxx.extract.web_investing as wi
import datetime as dt
import xxx.extract.web_cophieu68 as cp
import xxx.transform.tram_anh as xta
import xxx.job.parent as p
from shutil import copyfile

class daily_job(p.job_parent):
    def __init__(self, data_path: str, username: str, password: str, chrome_driver_path: str) -> None:
        super().__init__(data_path)
        self.chrome_driver_path = chrome_driver_path
        self.un = username
        self.pw = password

    def extract_data_from_api(self, data_year):
        '''get stock price & finance data from vn direct''' 
        try:
            mr = vd.mass_request(data_path = self.data_path, stock_symbol_list = self.stock_symbol_hose)
            mr.get_stock_price_year_range(symbols = self.stock_symbol_hose, start_y = data_year, end_y = data_year)
            mr.get_finance_data_year_range(symbols = self.stock_symbol_hose, start_y = data_year, end_y = data_year, type = "quarter")
            mr.get_stock_list()
            mr.get_finance_data_year_range(symbols = self.stock_symbol_hose, start_y = data_year, end_y = data_year, type = "year")
            copyfile(self.data_path + f"data/finance_data_quarter/finance_data_quarter_{data_year}.csv", self.data_path + f"data/finance_data_year/finance_data_quarter_{data_year}.csv")
            super().job_log("daily_job extract_data_from_api completed")
            return True
        except Exception as e:
            super().job_log(e)
            return False
    
    def extract_data_from_web(self):
        ''' get vnindex data from cophieu 68, get bond data from vn_investing '''
        try:
            ############### transform path
            data_path = self.data_path.replace("/", "\\")
            ############### get vnindex data from cophieu 68
            d_cp68 = cp.get_cophieu68(driver_path = self.chrome_driver_path, download_path = data_path + "data\\cophieu68", stock_url="https://www.cophieu68.vn/export/excelfull.php?id=^vnindex", un = self.un, pw = self.pw)
            d_cp68.close()
            ############### get bond data from vn_investing
            vn_investing = wi.web_scapping_vn_investing(driver_path = self.chrome_driver_path, download_path = data_path + "data\\vn_investing", un = self.un, pw = self.pw)
            d_vn_investing = vn_investing.get_government_bond_data_of_1_country(url = "https://vn.investing.com/rates-bonds/vietnam-10-year-bond-yield-historical-data", download_file_name = "vietnam_government_bond_data_10_years")
            d_vn_investing.close()
            super().job_log("daily_job extract_data_from_web completed")
            return True
        except Exception as e:
            super().job_log(e)
            return False

    def transform_data(self):
        '''standardize_vn_index_data, calculate beta, calculate ta  '''
        try:
            ############### standardize_vn_index_data
            vni.standardize_vn_index_data(self.data_path)
            ############### calculate beta
            today = dt.datetime.now().strftime('%Y-%m-%d')
            b = bt.calculate_beta(self.data_path, [today], 365)
            b.to_csv(self.data_path + f"data/beta/stock_beta_new.csv")
            ############### calculate ta
            calculate_ta = xta.xxx_tram_anh()
            calculate_ta.to_csv(self.stock_symbol_hose, self.data_path, history=False)
            calculate_ta.append_csv_vnindex(data_path= self.data_path)
            super().job_log("daily_job transform_data completed")
            # calculate_ta.to_csv(["HPG"], self.data_path, history=False)
            # calculate_ta.to_csv(self.stock_symbol_hose, self.data_path, history=True)
            return True
        except Exception as e:
            super().job_log(e)
            return False
