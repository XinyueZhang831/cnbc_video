########################################
# Web scraping all CNBC video id
# to support youtube_dl
########################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


def prepare_page(driver_dir, spagenumb, epagenumb):
    driver = webdriver.Chrome(driver_dir)
    driver.get('https://www.cnbc.com/video-ceo-interviews/')
    WebDriverWait(driver, 10)
    page_list = []

    for i in range(spagenumb,epagenumb+1):
        page_dir_make = 'https://www.cnbc.com/video-ceo-interviews/?page='+str(i)
        page_list.append(page_dir_make)

    video_df = pd.DataFrame()
    for page in page_list:
        driver.get(page)
        WebDriverWait(driver, 10)
        video_lines, driver = find_each_video_line(driver)
        videos = find_each_video(video_lines)
        video_df = video_df.append(videos, ignore_index=True)

    video_df.to_csv('CNBC_videoid.csv')


def find_each_video_line(driver):
    video_lines = driver.find_elements_by_css_selector("#pipeline_assetlist_0 > table > tbody")
    return video_lines, driver


def find_each_video(video_lines):
    df = pd.DataFrame()
    for line in video_lines:
        videos = line.find_elements_by_xpath('./tr')
        for video in videos:
            td = video.find_elements_by_xpath('./td')
            for each_td in td:
                video_id = each_td.find_element_by_xpath('./div/span/a')
                id_numb = video_id.get_attribute("data-videoid")
                video_url = video_id.get_attribute('href')
                data = {'video_url': video_url, 'video_id': id_numb}
                df = df.append(data, ignore_index=True)
    print('page finish')
    return df



driver_dir = '/Users/xinyue/PycharmProjects/web_scraping/driver/chromedriver'
spagenumb = 1
epagenumb = 38
prepare_page(driver_dir, spagenumb, epagenumb)