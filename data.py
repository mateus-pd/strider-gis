import rasterio
from rasterio import plot
import numpy
from affine import Affine
from pyproj import Proj, transform
import os
import datetime

path=r"/home/mateus/Projetos/strider-gis/analytic.tif"
rasterio_file = rasterio.open(path)

def tifFilename():
    return rasterio_file.name

def vegetationIndex():
    src = rasterio_file
    red = src.read(3)
    nir = src.read(4)
    # Allow division by zero
    numpy.seterr(divide='ignore', invalid='ignore')
    # Calculate NDVI
    ndvi = numpy.where((nir+red)==0., 0, (nir-red)/(nir+red))
    return ndvi.sum() / ndvi.size

def geoCentroid():
    # Get File
    src = rasterio_file
    T0 = src.profile["transform"]
    p1 = Proj(src.crs)
    A = src.read(1)
    cols, rows = numpy.meshgrid(numpy.arange(A.shape[1]), numpy.arange(A.shape[0]))
    T1 = T0 * Affine.translation(0.5, 0.5)
    rc2en = lambda r, c: (c, r) * T1
    eastings, northings = numpy.vectorize(rc2en, otypes=[numpy.float, numpy.float])(rows, cols)
    lon, lat = transform(p1, p1.to_latlong(), eastings, northings)
    return {"type": "Point", "coordinates": [(lon.sum() / lon.size), (lat.sum() / lat.size)]}

def calculateArea():
    #File
    src = rasterio_file
    width = src.bounds[2] - src.bounds[0] #kilometers
    height = src.bounds[3] - src.bounds[1] #kilometers
    return width * height

def tiffTimestamp():
    # Try to get the Timestamp from the "tif" file with GDAL, TAG "TIFFTAG_DATETIME"
    # but returns NoneType
    millis = os.path.getctime(path)
    return datetime.datetime.fromtimestamp(millis).isoformat()

def showImage():
    plot.show(rasterio_file, cmap="gray")