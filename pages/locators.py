from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "/html/body/div/div/div/header/div[1]/div[2]/a[2]")

class LoginPageLocators():
    EMAIL_FIELD = (By.ID, "passp-field-login")
    SIGN_IN_BUTTON = (By.ID, "passp:sign-in")
    PASSWORD_FIELD = (By.ID, "passp-field-passwd")

class MailPageLocators():
    DISK_LINK = (By.XPATH, "/html/body/div[3]/div[2]/div[7]/div/div[1]/div/div/div[2]/a[2]")

class DiskPageLocators():
    CREATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div[1]/div/div/span[2]/button")
    FOLDER_BUTTON = (By.XPATH, "/html/body/div[3]/div/button[1]")
    FOLDER_NAME_FIELD = (By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[1]/div/form/span/input")
    SAVE_FOLDER_BUTTON = (By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/button")
    CREATED_FOLDER = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[3]/div/div[1]")
    FILE_BUTTON = (By.XPATH, "/html/body/div[3]/div/button[2]")
    FOLDERS_NAME = (By.CLASS_NAME, "clamped-text")