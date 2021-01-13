"""
@file
@brief Test for :epkg:`cartopy`.
"""
import matplotlib.pyplot as plt


def check_cartopy():
    """
    Runs a sample with :epkg:`cartopy`.
    Returns a graph.
    """
    # delayed import to avoid failure
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([-5, 10, 42, 52])
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_title('France')
    return ax
