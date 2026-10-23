from bs4 import BeautifulSoup
import time

from app.scraper.driver import creer_driver


def recuperer_page(URL):
    browser = creer_driver()
    browser.get(URL)
    time.sleep(10)


    for _ in range(5):
        try:
            browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        except Exception as e:
            print("Défilement impossible :", e)
            break
        time.sleep(2)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    browser.quit()  
    return soup
