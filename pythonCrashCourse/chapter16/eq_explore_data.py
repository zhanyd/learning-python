import os
import json

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.realpath(__file__))
print("current_dir: " + current_dir)

filename = current_dir + "/data/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags, titles, lons, lats = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    title = eq_dict["properties"]["title"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]

    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10]) 
print(titles[:10])
print(lons[:10])
print(lats[:10])
