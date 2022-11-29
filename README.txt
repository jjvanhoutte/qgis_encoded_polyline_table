Just figuring out how to share this code.
It is obvoiously not clean and easy to use yet.

It depends greatly on the plugin by Ismail Sunni and the library by Frederick Jansen
Run the plugin first.

Put the polylinestrings in a table layer "all_routes" in a column "routePolyline"
Make sure you have the columns "id" and "outFileName" in your table layer as they will be copied to the new layer. 

Then run polylinegeom.py to define the function
Finally run convertlayer.
