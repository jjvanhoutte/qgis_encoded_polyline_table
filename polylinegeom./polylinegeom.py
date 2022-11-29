# This code is based on IsmailSunni's qgis_encoded_polyline
# dependencies are not all solved. Run his code or QGIS plugin first.
def polylinegeom(polyline_string):
    import codecs
    import importlib
#    if polyline_string[-1]=='\\':
#        polyline_string=polyline_string[0:-1]+'@'
    encoded = importlib.import_module("encoded-polyline")
#    polyline_string = codecs.decode(polyline_string, "unicode_escape")
    coordinates = encoded.polyline.decode(
        polyline_string, precision=5, geojson=True
    )
    qgis_coords = [QgsPointXY(x, y) for x, y in coordinates]
    geom = QgsGeometry.fromPolylineXY(qgis_coords)
    return geom
# Run the "encoded polyline" plugin before using this function
