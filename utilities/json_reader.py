# class JsonReader:
#
#     @staticmethod
#     def get_login_data(user_type):
#
#         with open(
#             "testdata/login_data.json",
#             "r"
#         ) as file:
#
#             data = json.load(file)
#
#         return data[user_type]

import json


class JsonReader:

    @staticmethod
    def get_data(file_name, data_type):

        with open(
                f"testdata/{file_name}",
                "r"
        ) as file:

            data = json.load(file)

        return data[data_type]

