import glob
import pandas as pd

total = pd.DataFrame()
for fn in glob.glob("*.csv"):
    part = pd.read_csv(fn, encoding="utf-8")
    total = pd.concat([total, part],
                      axis=0,
                      ignore_index=True)
# print("https:" + total["high_res_url"])

def get_sub(url):
    sub = url.split(".")[-1]
    return sub.lower()
new = total["high_res_url"].apply(get_sub)
print(new.value_counts())