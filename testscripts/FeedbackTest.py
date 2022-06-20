from selenium import webdriver
from time import sleep


def test_for_feedback():
    try:
        driver = webdriver.Chrome(r"C:\Users\nehas\Downloads\chromedriver_win32\chromedriver.exe")
        driver.get('http://localhost/Ems-devops-main/index.php')
        sleep(2)
        login_xpath = "/html/body/header/nav/div/ul/button"

        sleep(2)
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button_text = 'Login'
        assert login_button_text == login_button.text
        login_button.click()
        sleep(3)
        driver.find_element_by_xpath(
            '/html/body/header/nav/div/ul/div/div/div/div[2]/div/div/form/div[1]/input').send_keys('Mythri')
        driver.find_element_by_xpath(
            '/html/body/header/nav/div/ul/div/div/div/div[2]/div/div/form/div[2]/input').send_keys('mythri')
        sleep(3)
        login_xpath = "/html/body/header/nav/div/ul/div/div/div/div[2]/div/div/form/button"
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button.click()
        sleep(3)

        Feedback_xpath = "/html/body/header/nav/div/ul/li[7]/a"
        Feedback_button = driver.find_element_by_xpath(Feedback_xpath)
        Feedback_text = 'Feedback'
        assert Feedback_text == Feedback_button.text
        Feedback_button.click()

        Add_review_xpath = "/html/body/div/div/a"
        Add_review_button = driver.find_element_by_xpath(Add_review_xpath)
        Add_review_text = 'Add review'
        assert Add_review_text == Add_review_button.text
        Add_review_button.click()

        driver.find_element_by_name('Username').send_keys('Mythri')
        sleep(1)
        driver.find_element_by_name('Rev').send_keys('5')
        sleep(1)
        driver.find_element_by_name('Comment').send_keys('Great Experience')
        sleep(1)
        Add_feedback_xpath = "/html/body/div/div/form/button"
        Add_feedback_button = driver.find_element_by_xpath(Add_feedback_xpath)
        Add_feedback_button.click()
        sleep(1)

        Review_xpath = "/html/body/ul/li[7]/a"
        Review_button = driver.find_element_by_xpath(Review_xpath)
        Review_text = 'Reviews'
        assert Review_text == Review_button.text
        Review_button.click()
        sleep(1)






    finally:
        driver.close()