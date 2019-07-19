import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from seleniumDemo import  object_store

class Doclever(object):
    def __init__(self, p_driver):
        self.driver = p_driver
    #登陆doclever
    def login(self,p_user,p_pwd):
        self.new_find_element(object_store.login_link_new).click()
        self.new_find_element(object_store.login_user_new).clear()
        self.new_find_element(object_store.login_user_new).send_keys(p_user)
        self.new_find_element(object_store.login_pwd_new).clear()
        self.new_find_element(object_store.login_pwd_new).send_keys(p_pwd)
        self.new_find_element(object_store.login_btn_new).click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def new_find_element(self,p_obj):
        if p_obj.startswith('id'):
            return self.driver.find_element_by_id(p_obj.split('=')[1])
        elif p_obj.startswith('xpath'):
            return self.driver.find_element_by_xpath(p_obj[p_obj.index('=')+1:])
        elif p_obj.startswith('link text'):
            return self.driver.find_element_by_link_text(p_obj.split('=')[1])
        elif p_obj.startswith('name'):
            return self.driver.find_element_by_name(p_obj.split('=')[1])
        elif p_obj.startswith('tag name'):
            return self.driver.find_element_by_class_name(p_obj.split('=')[1])
        elif p_obj.startswith('css selector'):
            return self.driver.find_element_by_css_selector(p_obj.split('=')[1])
        elif p_obj.startswith('partial link text'):
            return self.driver.find_element_by_partial_link_text(p_obj.split('=')[1])
        else:
            return None