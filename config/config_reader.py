import os
import configparser

config_path = os.path.join(
    os.path.dirname(__file__),
    "config.ini"
)
config = configparser.ConfigParser()

config.read(config_path)

ENV = os.getenv("TEST_ENV", "QA")


class ConfigReader:

    @staticmethod
    def get_url():
        return config.get(ENV, "url")

    @staticmethod
    def get_heroku_url():
        return config.get(ENV, "heroku_url")

    @staticmethod
    def get_uber_supplier_url():
        return config.get(ENV, "company_url")

    @staticmethod
    def get_browser():
        return config.get(ENV, "browser")

    @staticmethod
    def get_username():
        return config.get(ENV, "username")

    @staticmethod
    def get_password():
        return config.get(ENV, "password")

    @staticmethod
    def get_uber_email():
        return config.get(ENV, "uber_email")

    @staticmethod
    def get_uber_password():
        return config.get(ENV, "uber_password")

    @staticmethod
    def get_clario_url():
        return config.get(ENV, "clario_url")




















# import configparser
# import os
#
# config = configparser.ConfigParser()
#
# config.read(
#     os.path.join(
#         os.path.dirname(__file__),
#         "config.ini"
#     )
# )
#
# class ConfigReader:
#
#     @staticmethod
#     def get_url():
#         return config.get("environment", "url")
#
#     @staticmethod
#     def get_browser():
#         return config.get("environment", "browser")
#
#     @staticmethod
#     def get_username():
#         return config.get("environment", "username")
#
#     @staticmethod
#     def get_password():
#         return config.get("environment", "password")