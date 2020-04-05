from selenium import webdriver
import time
import math

try:
    link = "http://www.combin.com/product/instagram-growth/#"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)

    # выключаем плашку с сообщением про кукис

    cookies_close = browser.find_element_by_class_name("icon__ic-cross").click()

    # 0
    growth = browser.find_element_by_id(0).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "View daily, weekly and monthly account activity statistics in-app. Track the followers count, see how many accounts followed and unfollowed you. Monitor the number of received likes and comments."

    # 1
    advanced = browser.find_element_by_id(1).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Find interesting profiles and publications by using and combining different search queries. Run searches by hashtag, location, specific account’s following, followers, likers and commenters, and by bio."

    # 2
    button2 = browser.find_element_by_id(2).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Specify the following and followers quantity, select male or female gender, and pick from a variety of languages the preferred ones. Define the target audience with precision using the demographic filters"

    # 3
    button3 = browser.find_element_by_id(3).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Identify low quality accounts with the help of the breakthrough technology. Eliminate pointless engagement and save the limited quantity of daily available actions for following, liking and commenting, to spend it on real, genuinely interested Instagram users"

    # 4
    button4 = browser.find_element_by_id(4).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Detect who doesn’t follow you back and unfollow them in convenient batches. Track the accounts you unfollowed and automatically prevent following them or interacting ever again. Protect important accounts from accidental unfollowing. Filter and export your user lists to Excel"

    # 5
    button5 = browser.find_element_by_id(5).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Engage multiple Instagram accounts and posts at once instead of manually interacting with the content of each separate user. Bulk-follow, unfollow, like and comment. Create comment templates for different topics and purposes, and leave them in batch"

    # 6
    button6 = browser.find_element_by_id(6).click()

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Engage multiple Instagram accounts and posts at once instead of manually interacting with the content of each separate user. Bulk-follow, unfollow, like and comment. Create comment templates for different topics and purposes, and leave them in batch"

    # next_button

    next_button = browser.find_element_by_css_selector("div.arrow-button.arrow-button--right.slick-arrow").click()

    # prev-button

    # prev_button = browser.find_element_by_css_selector("div.arrow-button.arrow-button--left.slick-arrow").click()

    # вводим почту
    email_for_start = browser.find_element_by_class_name("download-block__input ")
    email_for_start.send_keys("openmedia@mail.ru")

    # кликаем по чек боксу

    check_box = browser.find_element_by_css_selector("p.download-block__agreement-text").click()

    # кликаем по try free

    button_try = browser.find_element_by_css_selector(
        "span.link-with-arrow.link-with-arrow--primary-color.link-with-arrow--down-small:nth-child(2)").click()

    print("autotest pass")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()