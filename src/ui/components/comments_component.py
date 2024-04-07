from selenium.webdriver.remote.webelement import WebElement

from src.ui.components.base_component import BaseComponent


class CommentsClubComponent(BaseComponent):

    def __init__(self, node: WebElement) -> None:
        super().__init__(node)
        self.locators = {
            "comments_list": ("xpath", ".//div[@class='ant-comment-content-detail']"),
            "answer_to_comment": ("xpath", ".//button[contains(@class,'answer-comment')]")
        }

    def answer_to_comment(self):
        self.answer_to_comment.click_button()

    def get_all_comments_list(self) -> list[str]:
        return [comment.text for comment in self.comments_list]


