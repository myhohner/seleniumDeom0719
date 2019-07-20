# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, configparser,os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from seleniumDemo.bussiness_lib import Doclever


class Demo(unittest.TestCase):
    ini_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config = configparser.ConfigParser()
    config.read(ini_file)

    url = config['env1']['url']
    username = config['env1']['username']
    password = config['env1']['password']

    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.implicitly_wait(30)
    verificationErrors = []
    accept_next_alert = True

    do = Doclever(driver)

    def test_1_login(self):
        # 打开网页
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        # 完成登录
        self.do.login(self.username, self.password)
        time.sleep(5)
        # 判断登录后跳转
        self.assertTrue(self.is_element_present(By.ID, "tab-interface"))

    # 退出
    def test_2_logout(self):
        driver = self.driver
        ActionChains(driver).move_to_element(
            driver.find_element_by_css_selector('i.el-icon-caret-bottom.el-icon--right')).perform()  # 把鼠标放到元素上，其他的什么都不动
        time.sleep(1)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='帮助中心'])[1]/following::li[1]").click()
        time.sleep(5)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "登录"))
        driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


if __name__ == "__main__":
    unittest.main()
