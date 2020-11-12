import json
import demjson

s = "{name:'Elwing'}"
# json.loads(s)
result = demjson.decode(s)
print(result)