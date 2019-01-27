import pandas as pd
import xlrd

excel_file = pd.ExcelFile('stackoverflow.xlsx')
print(excel_file.sheet_names)

excel_df = excel_file.parse()
print(type(excel_df))
print(excel_df.head())

posts_excel = pd.read_excel('stackoverflow-one.xlsx')
print(posts_excel.columns)
print(posts_excel.head())
print(pd.read_excel('stackoverflow-one.xlsx', usecols=[0, 3]).columns)
print(pd.read_excel('stackoverflow-one.xlsx', usecols='A:C').columns)

#loading data from other sheets
posts_dict = pd.read_excel('stackoverflow.xlsx', sheet_name=None)
print(type(posts_dict))
print(posts_dict.keys())
print(posts_dict['Posts'].head())
print(pd.read_excel('stackoverflow.xlsx', sheet_name='Users', usecols=range(1,9)).head())

print(pd.read_excel('stackoverflow.xlsx', sheet_name='Users', converters={'Id': lambda x: x + 1000}).head())