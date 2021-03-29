import urllib
from urllib.request import urlopen
import json
import os
import random

ua_list = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        ]


txt = open(r"C:\Users\whl5378\Desktop\plaid_shirt.txt", 'rb')
search_list = txt.read()

m = 1
src_url_search = "https://api.unsplash.com/search/photos?client_id=a32c4f4092abfcd0e5b36d9cd72f0e201a1a1184742ffcc4907e81d67cf7da9b&per_page=20"
query = "plaid%20shirt"
if not os.path.isdir("F:\\329运动模糊\\unsplash_shirt\\" + query):
    os.makedirs("F:\\329运动模糊\\unsplash_shirt\\" + query)

search_list = str(search_list)

temp_start = 0
quote_end = -1
while temp_start != -1:
    temp_start = search_list.find('"raw"', quote_end + 1)
    quote_start = temp_start + 7
    quote_end = search_list.find(",", quote_start) - 1
    image_url = search_list[quote_start:quote_end]
    print(image_url)
    # image_url = urllib.request.quote(image_url, ':/=&?')
    response = urllib.request.urlopen(image_url)
    re = response.read()
    with open("F:\\329运动模糊\\unsplash_shirt\\" + query + "\\"
              + str(m) + ".jpg", 'wb') as f:
        f.write(re)
    m = m + 1
    temp_start = search_list.find('"raw"', quote_end + 1)

