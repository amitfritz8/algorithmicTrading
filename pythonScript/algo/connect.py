# -*- coding: utf-8 -*-
"""
Zerodha kiteconnect automated authentication

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from kiteconnect import KiteConnect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from pyotp import TOTP
import pyotp




cwd = os.chdir("/Users/amit/Documents/Python/PycharmProjects/AlgorithmicTrading/pythonScript")

def autologin():
  try:
    token_path = "api_key.txt"
    key_secret = open(token_path,'r').read().split()
    kite = KiteConnect(api_key=key_secret[0])



    # Set up Chrome options


    service = webdriver.chrome.service.Service('/opt/homebrew/bin/chromedriver')
    service.start()
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options = options.to_capabilities()
    driver = webdriver.Remote(service.service_url, options)
    driver.get(kite.login_url())
    driver.implicitly_wait(10)
    username = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
    username.send_keys(key_secret[2])
    password.send_keys(key_secret[3])
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    pin = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[1]/input')

    totp = pyotp.TOTP(key_secret[4])
    externalToken = totp.now()
    pin.send_keys(externalToken)
    time.sleep(10)

    """ WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/button'))
    ).click() """

    #driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[2]/button').click()
    time.sleep(10)
    request_token=driver.current_url.split('request_token=')[1][:32]
    with open('request_token.txt', 'w') as the_file:
        the_file.write(request_token)
    driver.quit()
  except Exception as e:
      print(f"An error occurred: {e}")
      driver.save_screenshot('error_screenshot.png')

  finally:
    driver.quit()

autologin()
