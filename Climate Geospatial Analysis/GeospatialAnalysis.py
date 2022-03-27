import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt


ds = xr.open_dataset('./Dataset/data.nc')

data = ds.isel(longitude=0, latitude=0).skt
data.plot()
plt.show()