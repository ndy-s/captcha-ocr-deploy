# Captcha OCR Deployment
This repository focuses on deploying Machine Learning models, specifically the model I've built to crack those pesky Captcha images (Captcha Optical Character Recognition). You know the ones—those squiggly letters and distorted numbers that pop up when you're trying to log in somewhere. They're like the vigilant bouncers at the internet club, ensuring that sneaky bots don't crash the party.

![Untitled](https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/e9ca4056-ad72-47b5-aefb-03785ab85265)

The dataset I used is sourced from Kaggle, specifically the [Captcha Version 2 Images](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images). However, here’s the catch: it’s a toy dataset. While it’s perfect for tinkering and learning, don’t expect it to handle real-world Captchas like a superhero.

Regarding the architecture, I've drawn inspiration from various sources. However, it seems there are some overfitting issues. Fear not—I might improve the model's performance in the future (hopefully...).

Okay, enough with the brief introduction. The deployment is divided into several parts. For now, I'm using tf-serving and flask deployment using the free deployment service [Railway](https://railway.app/). You'll get a free trial if you're new to Railway, so it's good for experimenting with deployment without worrying about costs. I might add some other deployment techniques and services like GCP or AWS in the future.

## Project Overview
The project repository contains several files and folders. I'll focus more on the deployment components:
1. `data` **Folder**: This directory stores the dataset used for training.
2. `model_deployment.ipynb`: This file contains the model development process. While I won’t delve into the details here, you can explore the comments and markdown within the notebook.
3. `models` **Folder**: Within this directory, you’ll find the trained model data and other assets necessary for prediction.
4. `Dockerfile`: An essential file that automates the deployment process.
5. `prediction_data` **Folder**: This directory holds unseen data, which is used to test the deployed model.
6. `model_prediction.ipynb`: A Jupyter notebook for testing the deployed model.
7. `app` **Folder**: This directory houses the Flask application responsible for captcha prediction. It offers an alternative approach for deploying the entire system and performing predictions.

## Setting Up Railway
Assuming you already have a Railway account, follow these steps to create a new project:
1. Log in to Railway.
2. Click on "Create Project".
3. Choose an empty project (you can name it as you like).

Now you’re ready to proceed with deploying your machine learning model using Railway!

## License
MIT
