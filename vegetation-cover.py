import data

def read() :
    return {
        "filename" : data.tifFilename(),
        "cover" : data.vegetationIndex(),
        "area" : data.calculateArea(),
        "centroid" : data.geoCentroid(),
        "local_time" : data.tiffTimestamp()
    }