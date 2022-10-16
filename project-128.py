import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests
def scrape():
    for i in range(1,5):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs=({"star", "constellation","right accension","decination","App.magnitude","Distance(ly)","spectral type","brown dwarf","mass(m)","radius(r)","orbital period(d)","semimajor axis(AU)","ecc"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        hyperlink_tag=li_tags[0]
        temp_list.append('https://en.wikipedia.org/wiki/List_of_brown_dwarfs'+hyperlink_tag.find_all('a',href=True)[0]['href'])
        brown_dwarfs_data.append(temp_list)
        browser.find_element(By.XPATH,'//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("c128.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(brown_dwarfs_data)
scrape()