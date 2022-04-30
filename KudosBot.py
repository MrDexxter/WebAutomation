from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time, os
import undetected_chromedriver.v2 as uc


def get_proxies():
    urls = ["https://free-proxy-list.net/",
            "https://us-proxy.org/", "https://socks-proxy.net/"]
    proxies = []
    for url in urls:
        soup = BeautifulSoup(requests.get(url).content, 'lxml')
        df = pd.read_html(str(soup.find("table")))[0]
        proxies += [str(ip) + ":" + str(p) for ip, p in zip(df["IP Address"].tolist(), df["Port"].tolist())]
    return proxies


def do_automation():
    global n
    proxies = get_proxies()
    print(f'WORKING ON New {len(proxies)}...')
    for prox in proxies:
        print("=" * 80)
        print(f"Proxy Number: {n}\nProxy Id: {prox}")
        print("=" * 80)
        options = uc.ChromeOptions()
        options.add_argument('--proxy-server=%s' % prox)
        browser = uc.Chrome(options=options)
        browser.refresh()
        try:
            browser.get("https://archiveofourown.org/works/35841298/chapters/89371996?view_adult=true")
            time.sleep(5)
            browser.find_element(By.XPATH, '/html/body/div[1]/div/p[2]/input').click()
        
        
        except:
            browser.close()
            continue
        time.sleep(3)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/p[3]/button').click()
        time.sleep(5)
        browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/ul/li[3]/form/input[4]').click()
        time.sleep(2)
        print("Kudos- Clicked")
        browser.close()
        clear()
        n = n + 1


clear = lambda: os.system('cls')

# ########################################### Main #######################################################


if __name__ == "__main__":
    n = 1
    while True:
        try:
            do_automation()
        except:
            pass
