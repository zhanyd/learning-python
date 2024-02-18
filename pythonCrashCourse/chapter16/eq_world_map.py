import os
import json
import plotly.express as px
import pandas as pd


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

print(lons[:10])
print(lats[:10])
print(mags[:10])
print(titles[:10])

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"])
data.head()

fig = px.scatter(
    data,
    x="经度",    
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=10,
    color="震级",
    hover_name = "位置"
)

fig.write_html('global_earthquakes.html')
fig.show()