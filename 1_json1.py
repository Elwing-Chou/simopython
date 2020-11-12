# import urllib.request
# urllib.request.urlopen()
# MAC: SSL cretificate fail
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
import os
from urllib.request import urlopen, urlretrieve

dirname = "google"
if not os.path.exists(dirname):
    os.makedirs(dirname)

for i in range(12):
    print("月份:", i+1)
    url = "https://www.google.com/doodles/json/2020/" + str(i+1) + "?hl=zh_TW"
    response = urlopen(url)
    pictures = json.load(response)

    for p in pictures:
        print(p["title"])
        imgurl = "https:" + p["url"]
        fn = imgurl.split("/")[-1]
        total = os.path.join(dirname, fn)
        urlretrieve(imgurl, total)