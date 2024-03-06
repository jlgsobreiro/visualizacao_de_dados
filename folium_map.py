import folium
from folium.plugins import Realtime

mapa = folium.Map(location=[-22.9140693, -43.5860686], tiles='CartoDB Positron', zoom_start=12)

folium.Circle(location=[-22.9008264, -43.5791618], radius=50, color='#3186cc', fill=True, fill_color='#3186cc').add_to(mapa)
folium.Marker([-22.9008264, -43.5791618], popup='<i>Sala 201</i>', tooltip='Clique aqui!').add_to(mapa)
# source = folium.JsCode("""
#     function onEachFeature(feature, layer) {
#         layer.bindPopup(feature.properties.description);
#     }
#     var geojson = L.geoJson(%s, {
#         onEachFeature: onEachFeature
#     });
#     this.addLayer(geojson);
# """ % open('Logradouros.json', 'r').read())
#
# real_time = Realtime(source, interval=1000)
# real_time.add_to(mapa)
mapa.save('mapa.html')
