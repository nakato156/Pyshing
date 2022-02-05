import selenium.webdriver as sl_web
from selenium import webdriver

class ScrapWebs():
    class FB():
        def __init__(self, driver:webdriver) -> None:
            self.driverFB = driver

        def acces(self, credentials:dict):
            self.driverFB.get("http://www.facebook.com")
            email = self.driverFB.find_element_by_id("email")
            passw = self.driverFB.find_element_by_id("pass")
            
            for c in credentials["username"]:
                email.send_keys(c)
            
            for c in credentials["password"]:
                passw.send_keys(c)
            self.driverFB.find_element_by_name("login").click()
            try:
                message = self.driverFB.find_element_by_class_name("_9ay7")
                msg = message.get_attribute("innerHTML")
            except:
                msg = None
            self.driverFB.quit()
            return msg

class Browser(ScrapWebs):
    def __init__(self, browser:str, executable_path:str) -> None:
        self.executable_path = executable_path

        options_driver = getattr(getattr(sl_web, browser.lower()), "options")
        Options = getattr(options_driver, "Options")
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu') 

        self.DRIVER = getattr(webdriver, browser)
    
    def init(self):
        self.driver:webdriver.Firefox = self.DRIVER(executable_path=self.executable_path, options=self.options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        return self