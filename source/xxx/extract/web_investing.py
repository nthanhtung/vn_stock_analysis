from selenium.webdriver.common.by import By
import time
from .web_scrapping import *
import xxx.utility as u

class web_scapping_vn_investing(web_scrapping):
    def __init__(self, driver_path: str, download_path: str, un: str = "x@gmail.com", pw: str = "******") -> None:
        #create foler if not exist
        stg_path = f"{download_path}\\stg"
        fnd_path = f"{download_path}\\fnd"
        super().__init__(driver_path=driver_path, download_path=stg_path)
        self.stg_path = stg_path
        self.fnd_path = fnd_path
        self.un = un
        self.pw = pw
    
    def get_government_bond_data_of_1_country(self, url, download_file_name):
        #create data dirs
        u.create_dir([self.stg_path,self.fnd_path])
        #launch browser
        driver = super().launch_browser()
        driver.get(url)
        #wait & close banner
        time.sleep(20)
        #close banner
        try:
            driver.find_elements(By.CLASS_NAME, 'popupCloseIcon.largeBannerCloser')[0].click()
            print("close banner")
        except:
            print("banner already closed")
        
        #login 
        try:
            driver.find_elements(By.CLASS_NAME, 'login.bold')[0].click()
            driver.find_elements(By.ID, 'loginFormUser_email')[0].send_keys(self.un)
            driver.find_elements(By.ID, 'loginForm_password')[0].send_keys(self.pw)
            driver.find_elements(By.CLASS_NAME, 'newButton.orange')[2].click()     
        except:
            print("already login")

        #select data & download
        driver.execute_script("window.scrollTo(0, 369)") 
        driver.find_elements(By.ID, 'datePickerIconWrap')[1].click()
        driver.find_elements(By.ID, 'startDate')[0].clear()
        driver.find_elements(By.ID, 'startDate')[0].send_keys("01/01/2000")
        driver.find_elements(By.ID, 'endDate')[0].clear()
        driver.find_elements(By.ID, 'endDate')[0].send_keys("01/01/2030")
        driver.find_elements(By.ID, 'applyBtn')[0].click()
        time.sleep(5)
        #retry download 3 times
        for i in range(3):
            driver.find_elements(By.CLASS_NAME, 'newBtn.LightGray.downloadBlueIcon.js-download-data')[0].click()
            time.sleep(i)
        #file operation
        u.copy_latest_file(source_dir = self.stg_path, target_dir = self.fnd_path, new_file_name = download_file_name)
        u.clean_dir(dirs = [self.stg_path])
        return driver
