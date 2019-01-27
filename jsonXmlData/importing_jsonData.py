import json
import requests

with open('posts-100.json') as f:
  posts_json = json.load(f)

print(type(posts_json))
print(len(posts_json))
print(posts_json[0])
print(type(posts_json[0]))

json_original = """
{
    "Id": 5,
    "PostTypeId": "1",
    "CreationDate": "2014-05-13T23:58:30.457",
    "Score": 9,
    "ViewCount": 448, 
    "LastActivityDate": "2014-05-14T00:36:31.077",
    "Title": "How can I do simple machine learning?",
    "Tags": "<machine-learning>",
    "AnswerCount": 1,
    "CommentCount": 1,
    "FavoriteCount": 1,
    "CloseDate": "2014-05-14T14:40:25.950"
}
"""

json_loaded = json.loads(json_original)
print(json_loaded)

print(json.dumps(json_loaded, indent=2))

this_tuple = ('one', 'two')
this_list = ['one', 'two']
json_tuple = json.dumps(this_tuple)
json_list = json.dumps(this_list)
print(json_tuple)
print(json_list)

print(json_tuple == json_list)

#importing data from a JSON API
# weather_query = 'https://query.yahooapis.com/v1/public/yql?q=select item.condition from weather.forecast where woeid = 2487889&format=json&env=store://datatables.org/alltableswithkeys'
# weather_call = requests.get(weather_query)
# weather = json.loads(weather_call.text)
# print(weather['query']['results']['channel']['item']['condition']['temp'])

