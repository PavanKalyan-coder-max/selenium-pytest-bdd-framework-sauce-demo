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
    def get_browser():
        return config.get(ENV, "browser")

    @staticmethod
    def get_username():
        return config.get(ENV, "username")

    @staticmethod
    def get_password():
        return config.get(ENV, "password")
























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