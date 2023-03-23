from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.mail_page import MailPage
from pages.disk_page import DiskPage
import time

def test_guest_can_create_document(browser):
    link = "https://mail.yandex.ru/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.fill_email_field()
    login_page.click_sign_in_button()
    login_page.fill_password_field()
    login_page.click_sign_in_button()
    mail_page = MailPage(browser, browser.current_url)
    mail_page.go_to_disk_page()
    disk_page = DiskPage(browser, browser.current_url)
    disk_page.click_create_button()
    disk_page.click_folder_button()
    disk_page.fill_folder_name_field()
    disk_page.click_create_folder_button()
    time.sleep(2)
    disk_page.go_to_created_folder()
    disk_page.click_create_button()
    disk_page.click_file_button()
    disk_page.fill_folder_name_field()
    disk_page.click_create_folder_button()
    disk_page.close_document_tab()
