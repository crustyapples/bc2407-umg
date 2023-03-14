from random import randint
import sys
import os
import numpy as np
import re
import json
import datetime
import selenium
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import urllib.request
import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

def opentiktok(song_name):
    options = Options()
    options.add_argument('profile-directory=Profile 10')
    options.add_argument("user-data-dir=C:\\Users\\ngwee\\AppData\\Local\\Google\\Chrome\\AutomationProfile")
    options.page_load_strategy = 'normal'
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    global driver

    try:
        if driver == None:
            driver = webdriver.Chrome(os.getcwd() + r'\chromedriver.exe', options=options)
    except:
        driver = webdriver.Chrome(os.getcwd() + r'\chromedriver.exe', options=options)
    driver.get(
        'https://www.google.com/search?q=' + song_name + ' site:https://www.tiktok.com/music')
    # while(True):
    #    pass



def click_options():
    option1 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="quickmatch-aria-tabpanel"]/div/div/div[1]/div[1]/div[2]/div[2]/button')))
    #option1 = driver.find_element_by_css_selector('h3 LC20lb DKV0Md'.replace(' ','.'))
    driver.execute_script("arguments[0].click();", option1)

def click_google_option():
    option1 = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'h3 LC20lb DKV0Md'.replace(' ','.'))))
    #option1 = driver.find_element_by_css_selector('h3 LC20lb DKV0Md'.replace(' ','.'))
    driver.execute_script("arguments[0].click();", option1)



def get_videos_created():
    option1 = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="main-content-single_song"]/div/div/div[1]/div[2]/h2[2]/strong')))
    return(option1.text)


def main():
    df = pd.read_csv('Tiktok dataset.csv')
    # opentiktok(df.iloc[0,3] +" "+ df.iloc[0,3])
    # click_google_option()
    # df.iloc[0,1] = get_videos_created()
    # df.to_csv(r"C:\Users\ngwee\OneDrive - Nanyang Technological University\Documents\NBS\BC2407 - ANALYTICS II ADV PRED TECH\Assignment\Final Folder\Tiktok dataset.csv")
    for i in range(27, 970):
        print(df.iloc[i,3])
        opentiktok(df.iloc[i,3] &" "& df.iloc[i,3])
        print(i)
        print(df.iloc[i,3] &" "& df.iloc[i,3])
        click_google_option()
        df.iloc[i,1] = get_videos_created()
        df.to_csv(r"C:\Users\ngwee\OneDrive - Nanyang Technological University\Documents\NBS\BC2407 - ANALYTICS II ADV PRED TECH\Assignment\Final Folder\Tiktok dataset.csv")

    


main()
