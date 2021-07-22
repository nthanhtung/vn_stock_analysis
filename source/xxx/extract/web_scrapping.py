from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class web_scrapping():
    def __init__(self, driver_path: str = "C:\\chromedriver_win32\\chromedriver.exe", download_path: str = "C:\\data") -> None:
        self.driver_path = driver_path
        self.download_path = download_path

    def launch_browser(self):
        '''
        config & launch chrome browser
        '''
        options = Options()
        options.add_experimental_option("prefs", {
        "download.default_directory": self.download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "safebrowsing.disable_download_protection": True
        })
        driver = webdriver.Chrome(executable_path = self.driver_path, options = options)
        return driver

