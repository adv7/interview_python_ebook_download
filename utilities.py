from selenium import webdriver
import pathlib
import os


def initialize_driver():
    download_dir = f"{pathlib.Path().absolute()}\\downloads"
    chrome_options = webdriver.ChromeOptions()
    prefs = {"plugins.always_open_pdf_externally": True, "download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    chromedriver = r'C:\Users\kryst\OneDrive\Dokumenty\selenium_drivers\chromedriver.exe'
    init_driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
    init_driver.get("https://www.salesmanago.com/")
    return init_driver


class FileManager:
    def __init__(self, file):
        self.file = file

    def is_file_downloaded(self):
        return os.path.isfile(f"{pathlib.Path().absolute()}\\downloads\\{self.file}")

    def delete_downloaded_file(self):
        os.remove(f"{pathlib.Path().absolute()}\\downloads\\{self.file}")
