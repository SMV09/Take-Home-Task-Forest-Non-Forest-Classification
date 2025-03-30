import streamlit as st
from streamlit_folium import st_folium
import folium
import rasterio
import rasterio.warp
import numpy as np

input_tif = "D:/Landsat/output_classified1/Classified_downsampled_image.tif"
output_tif = "D:/Landsat/output_classified1/Classified_downsampled_reprojected.tif"
image_name = "Classified_downsampled_reprojected.tif"  # Name of your classified image

with rasterio.open(input_tif) as src:
    dst_crs = 'EPSG:4326'  # Target CRS (latitude/longitude)
    transform, width, height = rasterio.warp.calculate_default_transform(
        src.crs, dst_crs, src.width, src.height, *src.bounds
    )
    kwargs = src.meta.copy()
    kwargs.update({
        'crs': dst_crs,
        'transform': transform,
        'width': width,
        'height': height
    })

    with rasterio.open(output_tif, 'w', **kwargs) as dst:
        for i in range(1, src.count + 1):
            rasterio.warp.reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=rasterio.warp.Resampling.nearest)

reprojected_tif = output_tif

with rasterio.open(reprojected_tif) as src:
    array = src.read(1)

    colormap = {
        0: [0, 0, 0],
        1: [0, 255, 0],
        2: [255, 0, 0],
    }

    rgb_array = np.zeros((array.shape[0], array.shape[1], 3), dtype=np.uint8)
    for class_label, color in colormap.items():
        rgb_array[array == class_label] = color

    bounds = src.bounds
    bbox = [(bounds.bottom, bounds.left), (bounds.top, bounds.right)]

st.title("Forest and Non-Forest classification!")
m = folium.Map(location=[-1.309, 110.20], zoom_start=6)


img = folium.raster_layers.ImageOverlay(
    name="Forest and non-forest classification",
    image=rgb_array, #np.moveaxis(array, 0, -1), # the rgb_array is already formatted correctly.
    bounds=bbox,
    opacity=0.9,
    interactive=True,
    cross_origin=False,
    zindex=1,
).add_to(m) #added .add_to(m)

folium.Html(html, script=True).add_to(m)

folium.LayerControl().add_to(m)

st_folium(m)