#web mapping

import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[25.60, 85.11], disable_3d=False, zoom_control=0)

fgv = folium.FeatureGroup(name="volcanoes")                                                                                      #making a feature group that can be used to add layers/attributes to map

col = None
for l, t, e in zip(lat, lon, elev):
    
    if e < 1000:
        col = 'green'
    elif e < 3000 and e >= 1000:
        col = 'orange'
    else:
        col = 'red'

    fgv.add_child(folium.CircleMarker(location=[l, t], popup=str(e)+"m", radius=5, 
    fill_color=col, color="grey",fill_opacity=1, fill=True))
    #fg.add_child(folium.Marker(location=[l ,t], popup=str(e)+" m", icon=folium.Icon(color=col, icon='info-sign')))              #popup = folium.Popup(str(elev), parse_html=True) -> for data containing apostrophy and other char

fgp = folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), style_function=lambda x: 
{'fillColor':'green' if x['properties']['POP2005']<=5000000 else 'yellow' if 5000000<x['properties']['POP2005']<=50000000 
else 'orange' if 50000000<x['properties']['POP2005']<=200000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("map11.html")