import switch_dir
import xxx.job.daily as d
import xxx.job.history as h
import datetime as dt

data_path = "C:/Users/tung.nguyen/Desktop/0 Project/stock/"
chrome_driver_path = "C:/chromedriver_win32/chromedriver.exe"
username = "thanhtung211995@gmail.com"
password = "BkkWwkaL123"
data_year = dt.datetime.now().year

# daily job - run daily
job1 = d.daily_job(data_path, username, password, chrome_driver_path)
job1.extract_data_from_api(data_year)
job1.extract_data_from_web()
job1.transform_data()

# history job - only need to run once
job2 = h.history_job(data_path)
job2.extract_data_from_api(start_y = 2010, end_y = 2020)
