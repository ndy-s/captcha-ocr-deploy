# Captcha OCR Deployment
Welcome to the Captcha OCR Deployment repository! This project focuses on deploying a machine learning model designed to crack those pesky Captcha images (Captcha Optical Character Recognition). You know the ones—those squiggly letters and distorted numbers that pop up when you're trying to log in somewhere. They're like the vigilant bouncers at the internet club, ensuring that sneaky bots don't crash the party.

![Captcha Prediction Example](https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/e9ca4056-ad72-47b5-aefb-03785ab85265)

The dataset used for training is sourced from Kaggle, specifically the [Captcha Version 2 Images](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images). However, here’s the catch: it’s a toy dataset. While it’s perfect for tinkering and learning, don’t expect it to handle real-world Captchas like a superhero.

Regarding the architecture, I've drawn inspiration from various sources. However, it seems there are some overfitting issues. Fear not—I might improve the model's performance in the future (hopefully...).

Okay, enough with the brief introduction. The deployment is divided into several parts. For now, I'm using tf-serving and flask deployment using the free deployment service [Railway](https://railway.app/). You'll get a free trial if you're new to Railway, so it's good for experimenting with deployment without worrying about costs. Additionally, Docker deployment is available. You can test it locally using Docker by following the instructions provided in the repository. I might add some other deployment techniques and services like GCP or AWS in the future.

## Project Overview
This repository contains several files and folders, with a primary focus on the deployment components:
1. `data` **Folder**: Contains the dataset used for training.
2. `model_deployment.ipynb`: This notebook documents the model development process. While detailed explanations are provided within the notebook, you can explore the comments and markdown cells for insights.
3. `models` **Folder**: Stores the trained model data and other assets necessary for prediction.
4. `Dockerfile.dev`: Used for deployment in a development environment.
5. `Dockerfile.prod`: Used for deployment in a production environment.
6. `railway.toml`: Custom configuration file for Railway deployment.
7. `prediction_data` **Folder**: Holds unseen data for testing the deployed model.
8. `model_prediction.ipynb`: A Jupyter notebook for testing the deployed model.
9. `app` **Folder**: Contains the Flask application responsible for captcha prediction. Offers an alternative approach for deploying the entire system and performing predictions.

## Getting Started
Let's set up the project:
1. Clone this repository to your local machine:
   ```
   git clone https://github.com/ndy-s/captcha-ocr-deploy.git
   ```
2. Navigate to the project folder:
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
4. Then click on "Add a Service" and choose an empty service (it will show a pop-up to apply the changes). After that, click "Deploy".
5. You need to install Railway CLI to interact with Railway from your local terminal. Follow the guide [here](https://docs.railway.app/guides/cli).
   
Now you’re ready to proceed with deploying your machine learning model using Railway!

### Railway TensorFlow Serving Model Deployment
To deploy the model using Railway:
1. Run `railway login` in your terminal. This will navigate you to the browser to log in.
2. If you haven't initialized a Railway project yet, run `railway init`. Otherwise, skip this step.
3. Next, link your project. You can find the command to do this in your Railway project dashboard. Click on "Set the project locally," and you'll find a command like this: `railway link xxxx-xxx-xxx-xxxx`. Replace `xxxx-xxx-xxx-xxxx` with your project ID.
4. To deploy your model, simply run `railway up` and wait for the deployment process to complete.
5. Once the deployment process is finished, you can generate a domain for your deployed model. You can find this option in your Railway project service settings. See the image below for reference:<br>
   <img src="https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/a0222d1c-9398-43e8-9f11-1798cf08514d" width="300">
6. After you have obtained your domain, you can access the model to see the metadata. Visit `{YOUR_GENERATED_DOMAIN}/v1/models/captcha-ocr-model/metadata` to view the metadata.
7. Once you have found the metadata, update the `api_url` variable in the `model_prediction.ipynb` file to your generated domain `{YOUR_GENERATED_DOMAIN}/v1/models/captcha-ocr-model:predict`, and run all the code to test predictions on your deployed model.

### Railway Flask Deployment
To deploy the Flask application on Railway:
1. Navigate to the `app` folder by running `cd app` in your terminal to move to the app folder.
2. Re-login and link to the Railway project using `railway login` and `railway init`. This instructs Railway to focus deployment in this folder, so it won't use Dockerfile outside the folder.
3. Run `railway up` to deploy your model and wait until the deploying finished.
4. After finished you can Access the generated domain, and you're all set! You can interact with the web service deployed using Railway. Upload some images from `prediction_data` folder to do some predictions on the deployed model.<br>
   <img src="https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/85635ab5-15f3-4e13-8ea3-da47f6041616" height="200">
   <img src="https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/80469823-36c3-47df-8b4a-42ff2add6e75" height="200">
   
## Docker Deployment
For Docker deployment, I've provided a Docker setup named `Dockerfile.dev` for development purposes. Before proceeding, ensure you have Docker Engine installed on your system. You can find the installation process [here](https://docs.docker.com/engine/install/). Assuming you already have Docker Desktop running on your PC.

### Docker Model Deployment
To deploy the model using Docker:
1. Make sure you're already in the project directory in your terminal, then what you need is build the docker image based on `Dockefile.dev` file. Run this command:
   ```
   docker build -t captcha-ocr-model -f Dockerfile.dev .
   ```
3. Once the image has finished building, all you need to do is run the image in a container. Use this command:
   ```
   docker run -p 8501:8501 captcha-ocr-model
   ```
5. After the image has been deployed, you can check the model metadata by visiting `localhost:8501/v1/models/captcha-ocr-model/metadata`.
6. Once you have retrieved the metadata, update the `api_url` variable in the `model_prediction.ipynb` file with your localhost port `localhost:8501/v1/models/captcha-ocr-model:predict`. Then, run all the code to test predictions on your deployed model.

### Docker Flask Deployment
To deploy the Flask application on Docker:
1. Navigate to the `app` folder by running `cd app` in your terminal to move to the app folder.
2. Build the Docker image based on the `Dockerfile.dev` file. Run this command:
   ```
   docker build -t captcha-flask-app -f Dockerfile.dev .
   ```
4. Once the image is built, all you need to do is run the image in a Docker container using this command:
   ```
   docker run -p 5000:5000 captcha-flask-app
   ```
6. Now, you can access the web service using the URL `localhost:5000`. Upload some images from the `prediction_data` folder to perform predictions on the deployed model.

## License
MIT
