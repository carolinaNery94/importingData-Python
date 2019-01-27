import csv
import pandas as pd
import re #expressoes regulares

print(csv.list_dialects())
with open('users-simple-five.csv') as csv_file:
  csv_header = csv.reader(csv_file, delimiter=',', quotechar='"')
  for row in csv_header:
    print(row)

#para deixar numero sem ser string, utilizamos quote_nonumeric
with open('users-simple-five.csv') as csv_file:
  csv_header = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
  for row in csv_header:
    print(row)

#load data as dictionary
field_names = ['Id', 'Reputation', 'Location', 'DisplayName']
with open('users-simple-five.csv') as csv_file:
  csv_dict_reader = csv.DictReader(csv_file, fieldnames=field_names)
  for row in csv_dict_reader:
    print(row['DisplayName'] + ' has a reputation of ' + row['Reputation'])

#Pandas support columns of different types
#on posts-100.csv we have integer, string, data..
posts_csv = pd.read_csv('posts-100.csv')
print(type(posts_csv))
print(posts_csv)

print(posts_csv.head()) #specify subset


#load with URL
remote_file = 'https://raw.githubusercontent.com/xmorera/sample-data/master/csv/posts-100.csv'
posts_url = pd.read_csv(remote_file, header=None)
print(posts_url.head())

#number of rows that you want to read
posts_small = pd.read_csv('posts-100.csv', nrows=3, skiprows=3)
print(posts_small)

posts_odd = pd.read_csv('posts-100.csv', skiprows=lambda x: x % 2 != 0)
print(posts_odd.head())

#specify which columns to load
posts_columns = pd.read_csv('posts-100.csv', usecols=[0,6,7,8])
print(posts_columns.head())

posts_no_header = pd.read_csv('posts-100.csv', header=None)
print(posts_no_header.columns)

posts_prefix = pd.read_csv('posts-100.csv', header=None, prefix='Col')
print(posts_prefix.columns)

header_fields = ['New_Id', 'New_PostTypeId', 'New_CreationDate', 'New_Score', 'New_ViewCount', 'New_LastActivityDate', 'New_Title', 'New_Tags', 'New_AnswerCount', 'New_CommentCount', 'New_FavoriteCount', 'New_ClosedDate']
posts_add_header = pd.read_csv('posts-100.csv', names=header_fields)
print(posts_add_header.columns)

post_header = pd.read_csv('posts-100-header.csv')
print(post_header.columns)
print(post_header[['Id', 'AnswerCount']].head())
print(pd.read_csv('posts-100-header.csv', header='infer').columns)
print(pd.read_csv('posts-100-header.csv', header=None).columns) #get Index
print(pd.read_csv('posts-100-header.csv', usecols=[0,1,2,7], dtype={'PostTypeId' : float}).dtypes)

#to apply functions on columns = converters
posts_tags = pd.read_csv('posts-100-header.csv', usecols=[0,1,2,7], converters={'Tags': lambda x: re.findall('<[A-Za-z0-9_-]*>', x)})
print(posts_tags.head(3))
print(type(posts_tags.iloc[1]['Tags']))

posts_date = pd.read_csv('posts-100-header.csv', usecols=[0,1,2,7])
print(type(posts_date['CreationDate'][0]))
posts_date = pd.read_csv('posts-100-header.csv', usecols=[0,1,2,7],parse_dates=['CreationDate'])
print(posts_date.dtypes)

#missing values
print(pd.read_csv('posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10], na_filter=False).head())

#TSV data
print(pd.read_csv('posts-100.tsv', sep='\t').head())