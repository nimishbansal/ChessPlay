from selenium import webdriver
browser=webdriver.Chrome("/home/nimish/PycharmProjects/so/internship/macroproject/chromedriver")
browser.get("https://nextchessmove.com/")

k=1
while True:
    browser.find_elements_by_css_selector(".radio")[k].click()
    z = browser.find_element_by_id("calculate-button")
    z.click()
    while True:
        z = browser.find_element_by_id("calculate-button")
        if  z.is_enabled():
            break
    move=browser.find_elements_by_css_selector("div div a span")[0]
    move.click()

    if k==1:
        k=0
    else:
        k=1
browser