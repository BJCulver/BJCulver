# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 17:58:08 2021

@author: bjcul_000
"""

#Midiworld Scraping

#%%
#Initialization

import os
import wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#%%
#Driver
class scraper():
    def __init__(self):
        self.driver=webdriver.Chrome('D:\Desktop\chromedriver\chromedriver.exe')
        self.driver.implicitly_wait(25)
        self.driver.get('https://www.midiworld.com/')
        
        self.links=[]
def search_bar(self, keyword='rock'):
        driver=self.driver
        #enter keyword in page
        driver.find_element_by_name('q').click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys(keyword)
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
    
def next_page(self):
        driver=self.driver
        driver.find_elements_by_xpath("//a[@class='nomark']")[-1].click()
        
def get_midi(self):
        driver=self.driver
        downloads=driver.find_elements_by_link_text('download')
        for link in downloads:
            self.links.append(link.get_attribute('href'))
#scrapers are just big things that scrape
def scraperino(self, location, keyword):          
         #init scraper
         #input keyword
         search_bar(self, keyword)
    
         get_midi(self)
         next_page(self)
    
         while (len(self.driver.find_elements_by_xpath("//a[@class='nomark']"))==2):
             get_midi(self)
             next_page(self)
         self.driver.quit()
         path=os.path.join(location, keyword)
         if(not os.path.isdir(path)):
             os.mkdir(path, 0o666)
         if ("https://www.midiworld.com/download/2515" in self.links):
             self.links.remove("https://www.midiworld.com/download/2515")
         for link in self.links: 
             wget.download(link, out=path)
#%%
s=scraper()

scraperino(s, "D:\Desktop\Music Project", "rock")
