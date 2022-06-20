from selenium import webdriver
from time import sleep


def test_locations():
    driver = webdriver.Chrome(r"C:\Users\nehas\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get('http://localhost/Ems-devops-main/index.php')
    sleep(3)
    about_xpath = '/html/body/header/nav/div/ul/li[2]/a'
    about_text = 'Locations'
    about_menu = driver.find_element_by_xpath(about_xpath)
    assert about_text == about_menu.text, "text not matching"
    print('expected text is matching')
    about_menu.click()
    print('Opening Locations page...')
    total_height = int(driver.execute_script("return document.body.scrollHeight/8"))

    for i in range(1, total_height, 1):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    view_details_xpath = "/html/body/div/div[3]/section/div/div[3]/button"
    view_details_button = driver.find_element_by_xpath(view_details_xpath)
    view_details_button.click()


    sleep(3)