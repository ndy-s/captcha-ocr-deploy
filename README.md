# Captcha OCR Deployment
This repository focuses on deploying Machine Learning models, specifically the model I've built to crack those pesky Captcha images (Captcha Optical Character Recognition). You know the ones—those squiggly letters and distorted numbers that pop up when you're trying to log in somewhere. They're like the vigilant bouncers at the internet club, ensuring that sneaky bots don't crash the party.

![Captcha Prediction Example](https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/e9ca4056-ad72-47b5-aefb-03785ab85265)

The dataset I used is sourced from Kaggle, specifically the [Captcha Version 2 Images](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images). However, here’s the catch: it’s a toy dataset. While it’s perfect for tinkering and learning, don’t expect it to handle real-world Captchas like a superhero.

Regarding the architecture, I've drawn inspiration from various sources. However, it seems there are some overfitting issues. Fear not—I might improve the model's performance in the future (hopefully...).

Okay, enough with the brief introduction. The deployment is divided into several parts. For now, I'm using tf-serving and flask deployment using the free deployment service [Railway](https://railway.app/). You'll get a free trial if you're new to Railway, so it's good for experimenting with deployment without worrying about costs. Additionally, Docker deployment is available. You can test it locally using Docker by following the instructions provided in the repository. I might add some other deployment techniques and services like GCP or AWS in the future.

## Project Overview
The project repository contains several files and folders. I'll focus more on the deployment components:
1. `data` **Folder**: This directory stores the dataset used for training.
2. `model_deployment.ipynb`: This file contains the model development process. While I won’t delve into the details here, you can explore the comments and markdown within the notebook.
3. `models` **Folder**: Within this directory, you’ll find the trained model data and other assets necessary for prediction.
4. `Dockerfile.dev`: This file is used for development using Docker deployment. It automates the deployment process in a development environment.
5. `Dockerfile.prod`: This file is used for production using Railway deployment. It automates the deployment process for production environments.
6. `railway.toml`: This is a custom configuration file used to explicitly specify the usage of the `Dockerfile.prod` file for railway deployment.
7. `prediction_data` **Folder**: This directory holds unseen data, which is used to test the deployed model.
8. `model_prediction.ipynb`: A Jupyter notebook for testing the deployed model.
9. `app` **Folder**: This directory houses the Flask application responsible for captcha prediction. It offers an alternative approach for deploying the entire system and performing predictions.

## Getting Started
Before we dive in, let's set up our project. Start by cloning this repository to your local machine. Run the following command in your terminal:
```
git clone https://github.com/ndy-s/captcha-ocr-deploy.git
```
Navigate to the project folder using:
```
cd captcha-ocr-deploy
```
Now that you're in the project folder, let's continue with the deployment process.

## Railway Deployment
### Setting Up Railway
Assuming you already have a Railway account, follow these steps to create a new project:
1. Log in to Railway.
2. Click on "Create Project".
3. Choose an empty project (you can name it as you like).
4. Then click on "Add a Service" and choose an empty service. After that, click "Deploy" (it will show a pop-up to apply the changes).
5. You need to install Railway CLI to interact with Railway from your local terminal. Follow the guide [here](https://docs.railway.app/guides/cli).
   
Now you’re ready to proceed with deploying your machine learning model using Railway!

### Railway TensorFlow Serving Model Deployment
To deploy the model using Railway, follow these steps:
1. Run `railway login` in your terminal. This will navigate you to the browser to log in.
2. After logging in, run `railway init`. If you haven't made a Railway project yet, do this step. Otherwise, you can **SKIP** it.
3. Next, link your project. You can find the command to do this in your Railway project dashboard. Click on "Set the project locally," and you'll find a command like this: `railway link xxxx-xxx-xxx-xxxx`. Replace `xxxx-xxx-xxx-xxxx` with your project ID.
4. To deploy your model, simply run `railway up` and wait for the deployment process to complete.
5. Once the deployment process is finished, you can generate a domain for your deployed model. You can find this option in your Railway project service settings. See the image below for reference:<br>
   <img src="https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/a0222d1c-9398-43e8-9f11-1798cf08514d" width="300">
6. After you have obtained your domain, you can access the model to see the metadata. Visit `{YOUR_GENERATED_DOMAIN}/v1/models/captcha-ocr-model/metadata` to view the metadata.
7. Once you have found the metadata, update the `api_url` variable in the `model_prediction.ipynb` file to your generated domain `{YOUR_GENERATED_DOMAIN}/v1/models/captcha-ocr-model:predict`, and run all the code to test predictions on your deployed model.

### Railway Flask Deployment
To deploy the Flask application on Railway, follow these steps:
1. Navigate to the `app` folder by running `cd .\app\` in your terminal to move to the app folder.
2. After that, relogin and link again to the Railway project, using `railway login` and `railway init`. This instructs Railway to focus deployment in this folder, so it won't use Dockerfile outside the folder.
3. Run `railway up` to deploy your model and wait until the deploying finished.
4. After finished you can Access the generated domain, and you're all set! You can interact with the web service deployed using Railway. Upload some images from `prediction_data` folder to do some predictions on the deployed model.<br>
   <img src="https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/85635ab5-15f3-4e13-8ea3-da47f6041616" height="200">
   <img src="https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/80469823-36c3-47df-8b4a-42ff2add6e75" height="200">
   
## Docker Deployment
For Docker deployment, I've provided a Docker setup named `Dockerfile.dev` for development purposes. Before proceeding, ensure you have Docker Engine installed on your system. You can find the installation process [here](https://docs.docker.com/engine/install/). Assuming you already have Docker Desktop running on your PC.

### Docker Model Deployment
To deploy the model using Docker, follow these steps:
1. Make sure you're already in the project directory in your terminal, then what you need is build the docker image based on `Dockefile.dev` file. Run this command `docker build -t captcha-ocr-model -f Dockerfile.dev .`.
2. Once the image has finished building, all you need to do is run the image in a container. Use this command `docker run -p 8502:8501 captcha-ocr-model`.
3. After the image has been deployed, you can check the model metadata by visiting `localhost:8502/v1/models/captcha-ocr-model/metadata`.
4. Once you have retrieved the metadata, update the `api_url` variable in the `model_prediction.ipynb` file with your localhost port `localhost:8502/v1/models/captcha-ocr-model:predict`. Then, run all the code to test predictions on your deployed model.

### Docker Flask Deployment
To deploy the Flask application on Docker, follow these steps:
1. Navigate to the `app` folder by running `cd ./app/` in your terminal to move to the app folder.
2. Build the Docker image based on the `Dockerfile.dev` file. Run this command `docker build -t captcha-flask-app -f Dockerfile.dev .`.
3. Once the image is built, all you need to do is run the image in a Docker container using this command `docker run -p 5001:5000 captcha-flask-app`.
4. Now, you can access the web service using the URL `localhost:5001`. Upload some images from the `prediction_data` folder to perform predictions on the deployed model.

## License
MIT
