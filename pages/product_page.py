from .locators import MainPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*MainPageLocators.COOKIES_CLOSE)
        to_cookies_close.click()

    def click_to_growth(self):
        to_growth = self.browser.find_element(*MainPageLocators.GROWTH)
        assert self.is_element_present(
            *MainPageLocators.GROWTH), "View daily, weekly and monthly account activity statistics in-app. Track the followers count, see how many accounts followed and unfollowed you. Monitor the number of received likes and comments."
        to_growth.click()

    def click_to_advanced(self):
        to_advanced = self.browser.find_element(*MainPageLocators.ADVANCED)
        assert self.is_element_present(
            *MainPageLocators.ADVANCED), "Find interesting profiles and publications by using and combining different search queries. Run searches by hashtag, location, specific account’s following, followers, likers and commenters, and by bio."
        to_advanced.click()

    def click_to_gender(self):
        to_gender = self.browser.find_element(*MainPageLocators.GENDER)
        assert self.is_element_present(
            *MainPageLocators.GENDER), "Specify the following and followers quantity, select male or female gender, and pick from a variety of languages the preferred ones. Define the target audience with precision using the demographic filters"
        to_gender.click()

    def click_to_machine(self):
        to_machine = self.browser.find_element(*MainPageLocators.MACHINE)
        assert self.is_element_present(
            *MainPageLocators.MACHINE), "Identify low quality accounts with the help of the breakthrough technology. Eliminate pointless engagement and save the limited quantity of daily available actions for following, liking and commenting, to spend it on real, genuinely interested Instagram users"
        to_machine.click()

    def click_to_audience(self):
        to_audience = self.browser.find_element(*MainPageLocators.AUDIENCE)
        assert self.is_element_present(
            *MainPageLocators.AUDIENCE), "Detect who doesn’t follow you back and unfollow them in convenient batches. Track the accounts you unfollowed and automatically prevent following them or interacting ever again. Protect important accounts from accidental unfollowing. Filter and export your user lists to Excel"
        to_audience.click()

    def click_to_repetitive(self):
        to_repetitive = self.browser.find_element(*MainPageLocators.REPETITIVE)
        assert self.is_element_present(
            *MainPageLocators.REPETITIVE), "Engage multiple Instagram accounts and posts at once instead of manually interacting with the content of each separate user. Bulk-follow, unfollow, like and comment. Create comment templates for different topics and purposes, and leave them in batch"
        to_repetitive.click()

    def click_to_multiple(self):
        to_multiple = self.browser.find_element(*MainPageLocators.MULTIPLE)
        assert self.is_element_present(
            *MainPageLocators.MULTIPLE), "Engage multiple Instagram accounts and posts at once instead of manually interacting with the content of each separate user. Bulk-follow, unfollow, like and comment. Create comment templates for different topics and purposes, and leave them in batch"
        to_multiple.click()
