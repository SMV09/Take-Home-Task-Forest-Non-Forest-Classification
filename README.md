# Take-Home-Task-Forest-Non-Forest-Classification 

This project implements a Convolutional Neural Network (CNN) for automated forest and non-forest classification from satellite imagery. It streamlines the classification process by automatically detecting images within a specified input folder and performing necessary preprocessing steps.

Workflow:

Automated Image Input: The system automatically scans the input folder for satellite images (e.g., Landsat GeoTIFFs).
Preprocessing:
Band Selection: Relevant spectral bands are selected for the classification task.
Cloud Masking: Cloud and cloud shadow pixels are identified and masked to minimize their impact on classification accuracy.
NDVI-Based Training Data Generation: A Normalized Difference Vegetation Index (NDVI) image is generated from the selected bands. This NDVI image is then thresholded to create a preliminary forest/non-forest classification, which is used as the training label data for the CNN.
CNN-Based Classification:
A CNN model is trained using the preprocessed satellite image bands as input features and the NDVI-derived forest/non-forest mask as training labels.
The trained CNN model is applied to the input satellite images to generate a refined forest/non-forest classification.
Output Visualization and Export:
The final classified image is visualized, with forest areas displayed in green and non-forest areas in red.
The classified image is exported as a GeoTIFF file, preserving georeferencing information.
