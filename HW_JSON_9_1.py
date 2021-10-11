import json

infile = open('US_fires_9_1.json', 'r')

FireData = json.load(infile)

brights, lats, lons = [],[],[]

for fires in FireData:
    bright = fires["brightness"]
    lat = fires["latitude"]
    lon = fires["longitude"]
    if bright >= 450:
        brights.append(bright)
        lats.append(lat)
        lons.append(lon)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat':lats,
    'marker':{
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]
my_layout = Layout(title="US Wildfires Sept 1-13")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='usfires9_1.html')
    

