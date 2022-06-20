from selenium import webdriver
from time import sleep


def test_events():
    driver = webdriver.Chrome(r"C:\Users\nehas\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('http://localhost/Ems-devops-main/index.php')
    sleep(2)
    about_xpath = '/html/body/header/nav/div/ul/li[1]/a'
    about_text = 'Home'
    about_menu = driver.find_element_by_xpath(about_xpath)
    assert about_text == about_menu.text, "text not matching"
    print('expected text is matching')
    about_menu.click()
    print('Opening Home page...')
    total_height = int(driver.execute_script("return document.body.scrollHeight/2"))

    for i in range(1, total_height, 1):
        driver.execute_script("window.scrollTo(0, {});".format(i))

    sleep(3)
    driver.close()