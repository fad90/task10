from .base_page import BasePage
from .locators import DiskPageLocators
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class DiskPage(BasePage):
    folder_name = "NNNNnnnnь"

    def click_create_button(self):
        create_button = self.browser.find_element(*DiskPageLocators.CREATE_BUTTON)
        create_button.click()

    def click_folder_button(self):
        folder_button = self.browser.find_element(*DiskPageLocators.FOLDER_BUTTON)
        folder_button.click()

    def fill_folder_name_field(self):
        folder_name_field = self.browser.find_element(*DiskPageLocators.FOLDER_NAME_FIELD)
        folder_name_field.clear()
        time.sleep(2)
        folder_name_field.send_keys(self.folder_name)

    def click_create_folder_button(self):
        create_folder_button = self.browser.find_element(*DiskPageLocators.SAVE_FOLDER_BUTTON)
        create_folder_button.click()

    # def find_all_folders_name(self):
    #     action = ActionChains(self.browser)
    #     folders_name = self.browser.find_elements(*DiskPageLocators.FOLDERS_NAME)
    #     for element in folders_name:
    #         if element.text == self.folder_name:
    #             self.browser.refresh()
    #             action.double_click(element)
    #             action.perform()

    def go_to_created_folder(self):
        created_folder = self.browser.find_element(*DiskPageLocators.CREATED_FOLDER)
        action = ActionChains(self.browser)
        action.double_click(created_folder)
        action.perform()

    def click_file_button(self):
        file_button = self.browser.find_element(*DiskPageLocators.FILE_BUTTON)
        file_button.click()

    def close_document_tab(self):
        window_name = self.browser.window_handles[1]
        self.browser.switch_to.window(window_name)
        self.browser.close()