########################################
# Web scraping each video's detail
# include video content, show name
# and potential host(s)
########################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


def prepare_page(driver_dir, video_id):
    driver = webdriver.Chrome(driver_dir)
    path = video_id

    df = pd.read_csv(path)
    df = find_detail(df,driver)
    df = host_name(df)
    df.to_csv('video_detail.csv')


def find_detail(df, driver):
    for i, r in df.iterrows():
        try:
            url = r['video_url']
            driver.get(url)
            WebDriverWait(driver, 10)
            df.at[i,'content'] = driver.find_element_by_css_selector(
                'div > div.ClipPlayer-clipPlayerIntro > div.ClipPlayer-clipPlayerIntroSummary').text
            df.at[i, 'show'] = driver.find_element_by_css_selector(
                'div > div.ClipPlayer-clipPlayerIntro > div.ClipPlayer-clipPlayerIntroSection > a').text
        except:
            pass
    return df


def host_name(df):
    dic_show = {}
    dic_show['MAD MONEY WITH JIM CRAMER'] = 'Jim Cramer'
    dic_show['CLOSING BELL'] = 'Sara Eisen / Wilfred Frost'
    dic_show['SQUAWK ALLEY'] = 'Jon Fortt / Morgan Brennan / Carl Quintanilla'
    dic_show['SQUAWK ON THE STREET'] = 'Jim Cramer / Sara Eisen / David Faber'
    dic_show['SQUAWK BOX'] = 'Joe Kernen / Steve Liesman / Andrew Ross Sorkin / Becky Quick'
    dic_show['HALFTIME REPORT'] = 'Scott Wapner'
    dic_show['THE EXCHANGE'] = 'Kelly Evansr'
    dic_show['POWER LUNCH'] = 'Kelly Evans / Tyler Mathisen'
    dic_show['WORLDWIDE EXCHANGE'] = 'Brian Sullivan'
    for i,r in df.iterrows():
        if r['show'] in dic_show.keys():
            df.at[i, 'Host'] = dic_show[r['show']]
    return df

driver_dir = ''
video_id = ''
prepare_page(driver_dir, video_id)