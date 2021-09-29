import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent=4)

print(eqdata["metadata"]["count"])

print(len(eqdata["features"]))

list_of_eqs = eqdata["features"]

mags = []
lats = []
longs = []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lat = eq["geometry"]["coordinates"][0]
    long = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lats.append(lat)
    longs.append(long)

print(mags)
print(lats)
print(longs)
'''
for magnitude in eqdata():
    print(eqdata["features"]["mag"])
'''