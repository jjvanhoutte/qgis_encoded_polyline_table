# Run the "encoded polyline" plugin before using this script
# Run the polylinegeom_dev.py also
layer_s = QgsProject.instance().mapLayersByName('all_routes')[0]
layer_d = QgsVectorLayer(
    "LineString?crs=epsg:4326&field=id:string(36)&field=name:string(80)",
    'newPolyLineGeom2',
    "memory",
)
pr = layer_d.dataProvider()
for feature_s in layer_s.getFeatures():
    print(feature_s["outFileName"])
    feature = QgsFeature()
    feature.setAttributes([feature_s["id"],feature_s["outFileName"]])
    feature.setGeometry(polylinegeom(feature_s["routePolyline"]))
    pr.addFeatures([feature])
layer_d.updateExtents()
QgsProject.instance().addMapLayer(layer_d)
# Zoom to the layer
iface.mapCanvas().setExtent(layer_d.extent())
