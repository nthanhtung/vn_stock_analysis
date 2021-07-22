import xxx.extract.api_vn_direct as vd
import xxx.job.parent as p
from shutil import copyfile

class history_job(p.job_parent):
    def extract_data_from_api(self, start_y, end_y):
        '''get stock price & finance data from vn direct''' 
        try:
            mr = vd.mass_request(data_path = self.data_path, stock_symbol_list = self.stock_symbol_hose)
            mr.get_stock_price_year_range(symbols = self.stock_symbol_hose, start_y = start_y, end_y = end_y)
            mr.get_finance_data_year_range(symbols = self.stock_symbol_hose, start_y = start_y, end_y = end_y, type = "quarter")
            mr.get_finance_data_year_range(symbols = self.stock_symbol_hose, start_y = start_y, end_y = end_y, type = "year")
            super().job_log("history_job extract_data_from_api completed")
            return True
        except Exception as e:
            super().job_log(e)
            return False
    