import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_guest_should_see_login_link_pass(browser):
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
   
    button1 = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")))
    
    assert button1
        
