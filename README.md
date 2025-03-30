# Take-Home-Task-Forest-Non-Forest-Classification 

This project implements a Convolutional Neural Network (CNN) for automated forest and non-forest classification from satellite imagery. It streamlines the classification process by automatically detecting images within a specified input folder and performing necessary preprocessing steps.

Workflow:

1) Automated Image Input detection:
   The system automatically scans the "input folder" for satellite images (e.g., Landsat GeoTIFFs).

2) Preprocessing:
   1) Band Selection: Relevant spectral bands are selected for the classification task.
   2) Cloud Masking: Cloud and cloud shadow pixels are identified and masked and saved in a new folder.

3) NDVI-Based Training Data Generation: A Normalized Difference Vegetation Index (NDVI) image is generated from the selected bands (Band3 and Band 4). This NDVI image is then thresholded to create a preliminary forest/non-forest classification, which is used as the training label data for the CNN.

4) CNN-Based Classification:
   A CNN model is trained using the preprocessed satellite image bands as input features and the NDVI-derived forest/non-forest mask as training labels.
    The trained CNN model is applied to the input satellite images to generate a refined forest/non-forest classification.

Note: To successfully train the model and generate a classified output, opted for the original Landsat imagery as it provided a dataset free of null values. The cloud masked Landsat images, which contained null values, were found to interfere with the model's processing, causing errors.

6) Batch processing (works efficiently on large raster data):
    The batch_predict function efficiently processes large images for machine learning prediction by dividing them into smaller, manageable batches. It first flattens the image into pixel features, then iterates through these batches, using a provided model to predict class labels. The results are stored and finally reshaped back into the original image dimensions, providing a pixel-wise classification output. This method is particularly useful for handling memory constraints when dealing with high-resolution or large raster data.

7) Output Visualization and Export: The final classified image is visualized, with forest areas displayed in green and non-forest areas in red. The classified image is exported as a GeoTIFF file, preserving georeferencing information.

8) Basic frontend  using Streamlit for visualizing: "Forest and non-forest classified output" image overlaid on Openstreet map (OSM) map interface. This can be visualized in jupyter-notebook or by using anaconda prompt and running "streamlit run mystreamlit_app.py"


# To run the code:
1) Download and open the "Forest & Non-Forest Classification_Final.ipynb" in jupyter-notebook and zipped "Landsat", which is input folder.
2) Modify the 'input folder' path to point to a directory with new Landsat images from different time intervals. For example: Change the code script with this pathname, 'input_folder = "D:/Landsat"'
3) Rest run the jupyter-notebook code.
4) To view myStreamlitapp.py, open an Anaconda prompt cmd,
      - set the environment name " conda activate -env_name" and
      - Type "streamlit run myStreamlitapp.py" then click on the local/8080 and webpage with webmap with "Forest and non-forest classified output"  image overlaid on Openstreet map (OSM) map interface will be displayed. 
