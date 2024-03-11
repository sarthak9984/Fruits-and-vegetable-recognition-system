# Fruit and Vegetable Recognition System using CNN

This project is a deep learning-based system for recognizing fruits and vegetables using Convolutional Neural Networks (CNN). It includes a trained model and a web application for interactive usage.

## Overview

The system utilizes deep learning techniques, specifically CNNs, to recognize various types of fruits and vegetables from input images.
The model has been trained on a dataset containing images of different fruits and vegetables. After training, the model can accurately classify input images into one of the predefined categories.

The web application built using Streamlit provides a user-friendly interface for users to upload images and get real-time predictions from the trained model. It allows users to interact with the recognition system without needing any deep learning expertise.

## Features

- **CNN Model:** Trained model capable of recognizing fruits and vegetables from images.
- **Streamlit Web Application:** User interface for interacting with the recognition system.
- **Real-time Prediction:** Users can upload images and receive instant predictions from the model.
- **Easy Integration:** The web application can be deployed easily and accessed from any web browser.

## Usage

To use the web application, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.
4. Access the web application through your browser.

## Dataset

The dataset used for training the model contains images of various fruits and vegetables. The dataset is not included in this repository due to its size. However, it can be obtained from kaggle.

## Model Training

The CNN model was trained using TensorFlow and Keras. Details about the architecture and training process can be found in the `train_model.ipynb` notebook.

## Dependencies

- Python 3.x
- TensorFlow
- Keras
- Streamlit

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.


