from selenium.webdriver.common.by import By

from src.ui.components.center_card_component import CenterCardComponent
from src.ui.components.club_card_component import ClubCardWithEditComponent
from src.ui.components.edit_user_pop_up.edit_user_pop_up import EditUserPopUp
from src.ui.components.pagination_component import PaginationComponent
from src.ui.pages.base_pages.base_page import BasePage

MY_PROFILE_TITLE = (By.XPATH, ".//div[@class='content-title']")
USER_AVATAR = (By.XPATH, ".//span[contains(@class, 'user-avatar')]")
USER_NAME = (By.XPATH, ".//div[@class='user-name']")
USER_ROLE = (By.XPATH, ".//div[@class='user-role']")
USER_PHONE = (By.XPATH, "./descendant::div[@class='user-phone-data']")
USER_EMAIL = (By.XPATH, "./descendant::div[@class='user-email-data']")
EDIT_PROFILE_BUTTON = (By.XPATH, "./descendant::span[text()='Редагувати профіль']")
MY_LESSONS_OR_CENTERS_DROPDOWN = (By.XPATH, ".//div[contains(@class, 'ant-select-selector')]")
MY_LESSONS_DROPDOWN_BUTTON = (By.XPATH, "//div[contains(@class, 'select-item')]//span[text()='гуртки']")
MY_CENTERS_DROPDOWN_BUTTON = (By.XPATH, "//div[contains(@class, 'select-item')]//span[text()='центри']")
ADD_BUTTON = (By.XPATH, ".//div[contains(@class, 'add-club-dropdown')]//button")
ADD_CLUB_BUTTON = (By.XPATH, "//div[contains(@class,'ant-dropdown')]/child::*[1]//div[text()='Додати гурток']")
ADD_CENTER_BUTTON = (By.XPATH, "//div[contains(@class,'ant-dropdown')]/child::*[1]//div[text()='Додати центр']")
EDIT_USER_MODAL_FORM = (By.XPATH, "./descendant::div[contains(@class, 'ant-modal css-13m256z user-edit')]//div["
                                  "@class='ant-modal-content']")
CLUB_CARDS_LIST_WEB_ELEMENTS = (By.XPATH, ".//div[contains(@class,'ant-card-body')]")
SWITCH_PAGINATION_WEB_ELEMENT = (By.XPATH, ".//ul[contains(@class,'ant-pagination') and contains(@class,'pagination')]")
CENTER_CARDS_LIST_WEB_ELEMENTS = (By.XPATH, ".//div[contains(@class,'center-card')]")

LEFT_SIDE_ROOT = (By.XPATH, ".//div[contains(@class, 'menu-component')]")

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._my_profile_title = None
        self._user_avatar = None
        self._user_name = None
        self._user_role = None
        self._user_phone = None
        self._user_email = None
        self._edit_profile_button = None
        self._my_lessons_or_centers_dropdown = None
        self._my_lessons_dropdown_button = None
        self._my_centers_dropdown_button = None
        self._add_button = None
        self._add_club_button = None
        self._add_center_button = None

        self._left_side_root = None

        self._club_cards_list_web_element = []
        self._switch_pagination_web_element = None
        self._center_cards_list_web_elements = None

    @property
    def my_profile_title(self):
        if not self._my_profile_title:
            self._my_profile_title = self.driver.find_element(*MY_PROFILE_TITLE)
        return self._my_profile_title

    @property
    def user_avatar(self):
        if not self._user_avatar:
            self._user_avatar = self.driver.find_element(*USER_AVATAR)
        return self._user_avatar

    @property
    def user_name(self):
        if not self._user_name:
            self._user_name = self.driver.find_element(*USER_NAME)
        return self._user_name

    @property
    def user_role(self):
        if not self._user_role:
            self._user_role = self.driver.find_element(*USER_ROLE)
        return self._user_role

    @property
    def user_phone(self):
        if not self._user_phone:
            self._user_phone = self.driver.find_element(*USER_PHONE)
        return self._user_phone

    @property
    def user_email(self):
        if not self._user_email:
            self._user_email = self.driver.find_element(*USER_EMAIL)
        return self._user_email

    @property
    def edit_profile_button(self):
        if not self._edit_profile_button:
            self._edit_profile_button = self.driver.find_element(*EDIT_PROFILE_BUTTON)
        return self._edit_profile_button

    def click_edit_profile_button(self) -> EditUserPopUp:
        self.edit_profile_button.click()
        return EditUserPopUp(self.driver.find_element(*EDIT_USER_MODAL_FORM))

    @property
    def my_lessons_or_centers_dropdown(self):
        if not self._my_lessons_or_centers_dropdown:
            self._my_lessons_or_centers_dropdown = self.driver.find_element(*MY_LESSONS_OR_CENTERS_DROPDOWN)
        return self._my_lessons_or_centers_dropdown

    def click_my_lessons_or_centers_dropdown(self):
        self._my_lessons_or_centers_dropdown.click()
        return self

    @property
    def my_lessons_dropdown_button(self):
        if not self._my_lessons_dropdown_button:
            self._my_lessons_dropdown_button = self.driver.find_element(*MY_LESSONS_DROPDOWN_BUTTON)
        return self._my_lessons_dropdown_button

    def click_my_lessons_dropdown_button(self):
        self._my_lessons_dropdown_button.click()
        return self

    @property
    def my_centers_dropdown_button(self):
        if not self._my_centers_dropdown_button:
            self._my_centers_dropdown_button = self.driver.find_element(*MY_CENTERS_DROPDOWN_BUTTON)
        return self._my_centers_dropdown_button

    def click_my_centers_dropdown_button(self):
        self._my_centers_dropdown_button.click()
        return self

    @property
    def add_button(self):
        if not self._add_button:
            self._add_button = self.driver.find_element(*ADD_BUTTON)
        return self._add_button

    def click_add_button(self):
        self._add_button.click()
        return self

    @property
    def add_club_button(self):
        if not self._add_club_button:
            self._add_club_button = self.driver.find_element(*ADD_CLUB_BUTTON)
        return self._add_club_button

    def click_add_club_button(self):
        self._add_club_button.click()
        return self

    @property
    def add_center_button(self):
        if not self._add_center_button:
            self._add_center_button = self.driver.find_element(*ADD_CENTER_BUTTON)
        return self._add_center_button

    def click_add_center_button(self):
        self._add_center_button.click()
        return self

    def club_cards_list(self):
        club_elements = self.driver.find_elements(*CLUB_CARDS_LIST_WEB_ELEMENTS)
        club_components = []
        for element in club_elements:
            club_components.append(ClubCardWithEditComponent(element))
        return club_components

    @property
    def center_cards_list(self):
        center_elements = self.driver.find_elements(*CENTER_CARDS_LIST_WEB_ELEMENTS)
        center_components = []
        for element in center_elements:
            center_components.append(CenterCardComponent(element))
        return center_components

    @property
    def switch_pagination_web_element(self):
        if not self._switch_pagination_web_element:
            self._switch_pagination_web_element = PaginationComponent(self.driver.find_element(*SWITCH_PAGINATION_WEB_ELEMENT))
        return self._switch_pagination_web_element
