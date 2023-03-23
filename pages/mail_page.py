from .base_page import BasePage
from .locators import MailPageLocators

class MailPage(BasePage):
    def go_to_disk_page(self):
        disk_link = self.browser.find_element(*MailPageLocators.DISK_LINK)
        disk_link.click()