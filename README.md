# Take-Home-Task-Forest-Non-Forest-Classification 

This project implements a Convolutional Neural Network (CNN) for automated forest and non-forest classification from satellite imagery. It streamlines the classification process by automatically detecting images within a specified input folder and performing necessary preprocessing steps.

Workflow:

1) Automated Image Input:
   The system automatically scans the input folder for satellite images (e.g., Landsat GeoTIFFs).

2) Preprocessing:
   Band Selection: Relevant spectral bands are selected for the classification task.
    Cloud Masking: Cloud and cloud shadow pixels are identified and masked to minimize their impact on classification accuracy.

3) NDVI-Based Training Data Generation: A Normalized Difference Vegetation Index (NDVI) image is generated from the selected bands. This NDVI image is then thresholded to create a preliminary forest/non-forest classification, which is used as the training label data for the CNN.

4) CNN-Based Classification:
   A CNN model is trained using the preprocessed satellite image bands as input features and the NDVI-derived forest/non-forest mask as training labels.
    The trained CNN model is applied to the input satellite images to generate a refined forest/non-forest classification.

5) Batch processing: The batch_predict function efficiently processes large images for machine learning prediction by dividing them into smaller, manageable batches. It first flattens the image into pixel features, then iterates through these batches, using a provided model to predict class labels. The results are stored and finally reshaped back into the original image dimensions, providing a pixel-wise classification output. This method is particularly useful for handling memory constraints when dealing with high-resolution imagery.

6) Model accuracy is checked:

7) Output Visualization and Export: The final classified image is visualized, with forest areas displayed in green and non-forest areas in red. The classified image is exported as a GeoTIFF file, preserving georeferencing information.

8) Basic frontend  using Streamlit for visualizing "Forest and non-forest classified output" and "NDVI" images overlaid on Openstreet map (OSM) map interface. 
