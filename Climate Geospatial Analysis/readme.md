#Climate Geospatial Data Analysis
## Data Description

Dimensions:    (longitude: 142, latitude: 89, expver: 2, time: 500)

Coordinates:
  * longitude  (longitude) float32  -82.0 -81.75 -81.5 ... -47.25 -47.0 -46.75
  * latitude   (latitude) float32  6.0 5.75 5.5 5.25 ... -15.5 -15.75 -16.0
  * expver     (expver) int32  1 5
  * time       (time) datetime64[ns] 1979-01-01 1979-02-01 ... 2020-08-01

Data variables:

  * lai_hv     (time, expver, latitude, longitude) float32 ...
    
  * skt        (time, expver, latitude, longitude) float32 ...
    
  * tp         (time, expver, latitude, longitude) float32 ...

Attributes:
    
    Conventions:  CF-1.6
    
    history:      2020-09-30 12:13:58 GMT by grib_to_netcdf-2.16.0: /opt/ecmw...