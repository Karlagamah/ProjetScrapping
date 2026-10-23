from selenium import webdriver


def creer_driver():
    options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(options=options)
    return browser
