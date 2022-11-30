# Run the "encoded polyline" plugin before using this script
# Run the polylinegeom_dev.py also
# 2022.11.30 - made length of target fiuelds dependent on source field
# The result is that the name includes the length argument (issue)
# 
layer_s = QgsProject.instance().mapLayersByName('all_routes')[0]
maxLenName=max(list(map(len,QgsVectorLayerUtils.getValues(layer_s,"outFileName",)[0])))+5
maxLenId=max(list(map(len,QgsVectorLayerUtils.getValues(layer_s,"id",)[0])))+5
layer_d = QgsVectorLayer(
    "LineString?crs=epsg:4326&field=id:string(maxLenId)&field=name:string(maxLenName)",
    'newPolyLineGeom2',
    "memory",
)
pr = layer_d.dataProvider()
for feature_s in layer_s.getFeatures():
    print(feature_s["out#FileName"])
    feature = QgsFeature()
    feature.setAttributes([feature_s["id"],feature_s["outFileName"]])
    feature.setGeometry(polylinegeom(feature_s["routePolyline"]))
    pr.addFeatures([feature])
layer_d.updateExtents()
QgsProject.instance().addMapLayer(layer_d)
# Zoom to the layer
iface.mapCanvas().setExtent(layer_d.extent())
