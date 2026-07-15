from utilities.excel_reader import ExcelReader

data = ExcelReader.get_login_data("standard_user")

print(data)
print(data["Username"])
print(data["Password"])