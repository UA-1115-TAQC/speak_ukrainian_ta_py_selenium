from selenium.webdriver.common.by import By

from src.ui.pages.base_pages.base_page import BasePage

SEARCH_INPUT = (By.XPATH, ".//input[contains(@class, 'input') and @placeholder='Пошук...']")
SELECTED_ITEM_DROPDOWN = (By.XPATH, ".//span[contains(@class, 'selection-item')]")
DROPDOWN = (By.XPATH, ".//div[contains(@class, 'select-dropdown')]")
NEW_FIRST_ITEM_DROPDOWN = (By.XPATH, ".//div[contains(@id, 'rc_select_2_list_0')]")
OLD_FIRST_ITEM_DROPDOWN = (By.XPATH, ".//div[contains(@id, 'rc_select_2_list_1')]")
SHOW_UNREAD_MESSAGE_ITEM = (By.XPATH, ".//span[text()='Показати тільки непрочитані повідомлення: ']")
SHOW_UNANSWERED_MESSAGE_ITEM = (By.XPATH, ".//span[text()='Повідомлення без відповіді: ']")
UNREAD_MESSAGES_SWITCH = (By.XPATH,
                          ".//span[text()='Показати тільки непрочитані повідомлення: ']/following-sibling::button//span[@class='ant-switch-inner']")
UNANSWERED_MESSAGES_SWITCH = (
By.XPATH, ".//span[text()='Повідомлення без відповіді: ']/following-sibling::button//span[@class='ant-switch-inner']")
NO_MESSAGE_TITLE = (By.XPATH, ".//div[contains(@class, 'noMessages')]")
MESSAGE_ELEMENTS = (By.XPATH, ".//ul[contains(@class, 'ant-list-items')]//div[contains(@class, 'collapse ')]")


class MessagePage(BasePage):
    def init(self, driver):
        super().init(driver)
        self._search_itput = None
        self._selected_item_dropdown = None
        self._dropdown = None
        self._new_first_item_dropdown = None
        self._old_first_item_dropdown = None
        self._show_undread_message_item = None
        self._show_unanswered_message_item = None
        self._no_message_title = None
        # todo ????????????
        self._message_elements = None

    #todo все протестити чи воно шукається по цим ікспасам
    @property
    def search_itput(self):
        if not self._search_itput:
            self._search_itput = self._driver.find_element(*SEARCH_INPUT)
        return self._search_itput

    def search_input_send_keys(self, keys):
        self._search_itput.send_keys(keys)

    @property
    def selected_item_dropdown(self):
        if not self._selected_item_dropdown:
            self._selected_item_dropdown = self._driver.find_element(*SELECTED_ITEM_DROPDOWN)
        return self._selected_item_dropdown

    @property
    def dropdown(self):
        if not self._dropdown:
            self._dropdown = self._driver.find_element(*DROPDOWN)
        return self._dropdown

    @property
    def new_first_item_dropdown(self):
        if not self._new_first_item_dropdown:
            self._new_first_item_dropdown = self._driver.find_element(*NEW_FIRST_ITEM_DROPDOWN)
        return self._new_first_item_dropdown