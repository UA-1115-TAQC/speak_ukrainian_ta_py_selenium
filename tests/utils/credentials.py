import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:

    @staticmethod
    def get_url() -> str:
        return os.getenv("BASE_URL")

    @staticmethod
    def get_admin_email() -> str:
        return os.getenv("ADMIN_EMAIL")

    @staticmethod
    def get_admin_password() -> str:
        return os.getenv("ADMIN_PASSWORD")

    @staticmethod
    def get_manager_email() -> str:
        return os.getenv("MANAGER_EMAIL")

    @staticmethod
    def get_manager_password() -> str:
        return os.getenv("MANAGER_PASSWORD")

    @staticmethod
    def get_user_email() -> str:
        return os.getenv("USER_EMAIL")

    @staticmethod
    def get_user_password() -> str:
        return os.getenv("USER_PASSWORD")
