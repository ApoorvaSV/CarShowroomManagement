from selenium import webdriver
from time import sleep
def test_for_booking():
    try:
        driver = webdriver.Chrome(r"C:\Users\nehas\Downloads\chromedriver_win32\chromedriver.exe")
        driver.get('http://localhost/Ems-devops-main/index.php')
        driver.maximize_window()
        sleep(3)
        login_xpath = "/html/body/header/nav/div/ul/button"

        sleep(3)
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button_text = 'Login'
        assert login_button_text == login_button.text
        login_button.click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/header/nav/div/ul/div/div/div/div[2]/div/div/form/div[1]/input').send_keys('Mythri')
        driver.find_element_by_xpath('/html/body/header/nav/div/ul/div/div/div/div[2]/div/div/form/div[2]/input').send_keys('mythri')
        sleep(3)
        login_xpath = "/html/body/header/nav/div/ul/div/div/div/div[2]/div/div/form/button"
        login_button = driver.find_element_by_xpath(login_xpath)
        login_button.click()
        sleep(3)
        booking_xpath='/html/body/header/nav/div/ul/li[6]/a'
        booking_button = driver.find_element_by_xpath(booking_xpath)
        booking_button_text = 'Bookings'
        assert booking_button_text == booking_button.text
        booking_button.click()
        sleep(3)

        Book_an_event_xpath = "/html/body/div/div/a"
        Book_an_event_button = driver.find_element_by_xpath(Book_an_event_xpath)
        Book_an_event_text = 'Book an Event'
        assert Book_an_event_text == Book_an_event_button.text
        Book_an_event_button.click()
        driver.find_element_by_name('FullName').send_keys('Mythri M')
        sleep(1)
        driver.find_element_by_name('Username').send_keys('Mythri')
        sleep(1)
        driver.find_element_by_name('Email').send_keys('mythri@gmail.com')
        sleep(1)
        driver.find_element_by_name('Events').send_keys('Birthday')
        sleep(1)
        driver.find_element_by_name('Venue').send_keys('The Ritz Caltron')
        sleep(1)
        driver.find_element_by_name('EventDate').send_keys('06-07-2022')
        sleep(1)
        driver.find_element_by_name('NoOfHeads').send_keys('20')
        sleep(1)
        driver.find_element_by_name('Decoration').send_keys('Contemporary')
        sleep(1)
        driver.find_element_by_name('FoodStyle').send_keys('Mexican')
        sleep(1)


        Book_now_xpath = "/html/body/div/div/form/button"
        Book_now_button = driver.find_element_by_xpath(Book_now_xpath)
        Book_now_button.click()
        sleep(2)

        Bookings_xpath = "/html/body/ul/li[6]/a"
        Bookings_button = driver.find_element_by_xpath(Bookings_xpath)
        Bookings_text = 'Bookings'
        assert Bookings_text == Bookings_button.text
        Bookings_button.click()
        sleep(2)
        total_height = int(driver.execute_script("return document.body.scrollHeight/6"))

        for i in range(1, total_height, 1):
            driver.execute_script("window.scrollTo(0, {});".format(i))
        sleep(1)


    finally:
        driver.close()