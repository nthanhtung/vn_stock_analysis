import xxx.extract.api_vn_direct as vd
import logging

class job_parent():
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path
        self.stock_symbol_hose = vd.get_stock_symbol_hose(data_path)   
        pass
    def job_log(self, message_to_log):
        logging.basicConfig(filename=self.data_path + "data/job_log.txt",
                                    filemode='a',
                                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                    datefmt='%Y-%m-%d,%H:%M:%S',
                                    level=logging.DEBUG)
        logging.info(message_to_log)
        pass
    pass