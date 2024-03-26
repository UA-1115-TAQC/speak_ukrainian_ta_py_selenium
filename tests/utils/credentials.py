import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:

    @classmethod
    def get_url(cls) -> str:
        return os.getenv("BASE_URL")

    @classmethod
    def get_admin_email(cls) -> str:
        return os.getenv("ADMIN_EMAIL")

    @classmethod
    def get_admin_password(cls) -> str:
        return os.getenv("ADMIN_PASSWORD")

    @classmethod
    def get_manager_email(cls) -> str:
        return os.getenv("MANAGER_EMAIL")

    @classmethod
    def get_manager_password(cls) -> str:
        return os.getenv("MANAGER_PASSWORD")

    @classmethod
    def get_user_email(cls) -> str:
        return os.getenv("USER_EMAIL")

    @classmethod
    def get_user_password(cls) -> str:
        return os.getenv("USER_PASSWORD")
